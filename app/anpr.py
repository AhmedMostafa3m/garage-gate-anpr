
import cv2
import numpy as np
import easyocr
from app.config import CASCADE_PATH


class LicensePlateRecognizer:
    """
    Handles license plate detection and recognition using OpenCV + EasyOCR.
    """
    def __init__(self):
        # Load Haar Cascade for plate detection
        self.cascade = cv2.CascadeClassifier(CASCADE_PATH)
        # Initialize EasyOCR reader (English letters + digits)
        self.reader = easyocr.Reader(['en'], gpu=False)

    def recognize_plate(self, image):
        """
        Detects license plates, extracts text, and returns:
            - annotated_image: image with detection boxes and recognized text
            - detected_plates: list of recognized plate strings
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plates = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        detected_plates = []

        for (x, y, w, h) in plates:
            # Draw bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Crop the detected plate area
            plate_roi = gray[y:y + h, x:x + w]

            # Optional preprocessing for OCR
            plate_roi = cv2.bilateralFilter(plate_roi, 11, 17, 17)
            plate_roi = cv2.threshold(plate_roi, 150, 255, cv2.THRESH_BINARY)[1]

            # Run OCR
            ocr_result = self.reader.readtext(plate_roi)

            # Extract recognized text
            for (bbox, text, conf) in ocr_result:
                cleaned_text = self._clean_plate_text(text)
                if cleaned_text:
                    detected_plates.append(cleaned_text)
                    # Display recognized text on the image
                    cv2.putText(image, cleaned_text, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        return image, detected_plates

    def _clean_plate_text(self, text: str):
        """
        Removes unwanted characters from OCR output.
        Keeps only alphanumeric characters and converts to uppercase.
        """
        import re
        cleaned = re.sub(r'[^A-Z0-9]', '', text.upper())
        return cleaned if len(cleaned) >= 4 else None


if __name__ == '__main__':
    # Standalone test mode
    recognizer = LicensePlateRecognizer()
    image = cv2.imread('test_image.jpg')

    if image is None:
        print("❌ Error: test_image.jpg not found.")
    else:
        annotated, plates = recognizer.recognize_plate(image)
        print(f"Detected plates: {plates}")

        cv2.imshow('License Plate Recognition', annotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
