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

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Edge detection to find contours
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area and keep the largest one (assumes receipt is the largest object)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    receipt_contour = None
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # If the polygon has 4 points, it might be the receipt
        if len(approx) == 4:
            receipt_contour = approx
            break

    if receipt_contour is None:
        raise ValueError("Could not find a rectangular receipt in the image.")

    # Get a consistent order of points and prepare for a perspective transform
    rect = np.array(receipt_contour[:, 0], dtype="float32")
    rect = sorted(rect, key=lambda x: x[1])  # Sort by vertical (y-coordinate)

    # Top-left, top-right, bottom-right, bottom-left
    if rect[0][0] < rect[1][0]:  # Compare x-coordinates
        top_left, top_right = rect[0], rect[1]
    else:
        top_left, top_right = rect[1], rect[0]

    if rect[2][0] < rect[3][0]:  # Compare x-coordinates
        bottom_left, bottom_right = rect[2], rect[3]
    else:
        bottom_left, bottom_right = rect[3], rect[2]

    # Define the destination points for the perspective transform
    width = max(
        int(np.linalg.norm(top_right - top_left)),
        int(np.linalg.norm(bottom_right - bottom_left))
    )
    height = max(
        int(np.linalg.norm(top_left - bottom_left)),
        int(np.linalg.norm(top_right - bottom_right))
    )
    dst = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]
    ], dtype="float32")

    # Perspective transform to extract the receipt
    M = cv2.getPerspectiveTransform(np.array([top_left, top_right, bottom_right, bottom_left]), dst)
    warped = cv2.warpPerspective(image, M, (width, height))

    # Resize the extracted receipt (optional)
    resized = cv2.resize(warped, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Save the processed images
    cropped_filename = os.path.join(savePath, 'cropped_receipt.jpeg')
    resized_filename = os.path.join(savePath, 'resized_receipt.jpeg')
    cv2.imwrite(cropped_filename, warped)
    cv2.imwrite(resized_filename, resized)

    return resized

# Example usage
binarize('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# inverted = monoChrome('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# deskew('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# rotated = deskew('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')
# resize(rotated)
binarize('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')