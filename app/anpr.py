import cv2
import numpy as np

class LicensePlateRecognizer:
    def __init__(self):
        self.cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

    def recognize_plate(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plates = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in plates:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return image

if __name__ == '__main__':
    recognizer = LicensePlateRecognizer()
    image = cv2.imread('test_image.jpg')
    result = recognizer.recognize_plate(image)
    cv2.imshow('License Plate Recognition', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()