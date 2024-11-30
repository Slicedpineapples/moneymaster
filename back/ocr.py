import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import re
import json
# numpy
import os

global savePathGlobal
savePathGlobal = '/home/pc52/myprojects/moneymaster/back/test'

def monoChrome(imagePath):
    # Ensure the save directory exists
    savePath = savePathGlobal
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

def deskew(imagePath):
    savePath = savePathGlobal
    os.makedirs(savePath, exist_ok=True)

    # Load the image in grayscale mode
    inverted = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    if inverted is None:
        raise FileNotFoundError(f"Image not found at {imagePath}")

    # Find all non-zero pixel coordinates
    coords = np.column_stack(np.where(inverted > 0))
    angle = cv2.minAreaRect(coords)[-1]

    # Correct the angle
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # Get image dimensions
    (h, w) = inverted.shape[:2]
    center = (w // 2, h // 2)

    # Compute the rotation matrix and apply it
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(inverted, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Save the processed image
    filename = f'rotated_{os.path.basename(imagePath)}'
    outputPath = os.path.join(savePath, filename)
    cv2.imwrite(outputPath, rotated)

    return rotated

def resize(imagePath):
    savePath = savePathGlobal
    os.makedirs(savePath, exist_ok=True)

    # Load the image
    image = cv2.imread(imagePath)
    if image is None:
        raise FileNotFoundError(f"Image not found at {imagePath}")

    # Resize the image
    resized = cv2.resize(image, (1000, 1000))

    # Save the processed image
    filename = f'resized_{os.path.basename(imagePath)}'
    outputPath = os.path.join(savePath, filename)
    cv2.imwrite(outputPath, resized)

    return resized


# Example usage
# binarize('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# inverted = monoChrome('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# deskew('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# rotated = deskew('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# resize(rotated)
# binarize('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# resize('/home/pc52/myprojects/moneymaster/back/test/gray_rec4.jpeg')