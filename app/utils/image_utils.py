# app/utils/image_utils.py

import cv2

def preprocess_image(image):
    """Convert image to grayscale and apply histogram equalization."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return gray
