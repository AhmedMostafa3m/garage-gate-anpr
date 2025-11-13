import cv2
from app.anpr import LicensePlateRecognizer
from app.database import Database
from app.controller import GateController
from app.utils.image_utils import preprocess_image


def main():
    print("🚗 Starting Garage Access Control System...")
    db = Database()
    recognizer = LicensePlateRecognizer()
    controller = GateController()

    # Example: Add authorized plates (you can later manage this via a GUI or CLI)
    db.add_plate("ABC1234")
    db.add_plate("XYZ9876")

    # Load a test image (replace this with live camera feed later)
    image = cv2.imread("test_image.jpg")
    if image is None:
        print("❌ Error: test_image.jpg not found in project root.")
        controller.cleanup()
        return

    # Preprocess for better detection
    processed = preprocess_image(image)

    # Detect and recognize plates
    annotated_image, detected_plates = recognizer.recognize_plate(processed)

    if not detected_plates:
        print("⚠️ No license plates detected.")
    else:
        print(f"🔍 Detected plates: {detected_plates}")

        # Check each detected plate
        authorized = False
        for plate in detected_plates:
            if db.is_authorized(plate):
                print(f"✅ Plate {plate} is authorized. Opening gate...")
                controller.open_gate()
                authorized = True
                break  # No need to check others once gate opens
            else:
                print(f"🚫 Plate {plate} is NOT authorized.")

        if not authorized:
            print("❌ No authorized plates detected. Access denied.")

    # Show image with detection and recognized text
    cv2.imshow("License Plate Recognition", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    controller.cleanup()
    print("🟢 System shutdown complete.")


if __name__ == "__main__":
    main()

