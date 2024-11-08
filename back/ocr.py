import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import re
import json
# numpy
import os

def monoChrome(imagePath):
    # Ensure the save directory exists
    savePath = '/home/pc52/myprojects/moneymaster/back/test'
    os.makedirs(savePath, exist_ok=True)
    
    # Load the image in grayscale
    gray = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise ValueError(f"Unable to load the image from path: {imagePath}")
    
    # Apply adaptive thresholding for dynamic binarization
    gray = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 11
    )
    # Invert the binary image
    inverted = cv2.bitwise_not(gray)

    # Save the processed image
    filename = f'gray_{os.path.basename(imagePath)}'
    savePath = os.path.join(savePath, filename)
    cv2.imwrite(savePath, inverted)
    
    return inverted

# Example usage
processed_image = monoChrome('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
