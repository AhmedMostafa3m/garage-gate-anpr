# app/main.py

import cv2
from app.anpr.py import LicensePlateRecognizer
from app.database import Database
from app.controller import GateController
from app.utils.image_utils import preprocess_image


def main():
    db = Database()
    recognizer = LicensePlateRecognizer()
    controller = GateController()

    # Example: authorize some plates manually
    db.add_plate("ABC1234")

    # Load test image (replace with video/camera in production)
    image = cv2.imread("test_image.jpg")
    if image is None:
        print("❌ Error: test_image.jpg not found.")
        return

    processed = preprocess_image(image)
    result = recognizer.recognize_plate(processed)

    # Here, integrate OCR (you can use EasyOCR or PaddleOCR to extract plate text)
    # For now, we’ll simulate:
    detected_plate = "ABC1234"  # Placeholder for real OCR result

    if db.is_authorized(detected_plate):
        print(f"✅ Plate {detected_plate} authorized — opening gate.")
        controller.open_gate()
    else:
        print(f"🚫 Plate {detected_plate} not authorized — access denied.")

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    controller.cleanup()


if __name__ == "__main__":
    main()
