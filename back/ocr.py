import cv2
import pytesseract
from pytesseract import Output

def preprocessImage(image_path):
    # grasycale the image for better OCR accuracy
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize image to improve OCR accuracy
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    # Apply GaussianBlur to reduce noise 
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # Apply thresholding to binarize the image
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
    # resized = cv2.imshow('image', img)
    # cv2.waitKey(100000)
    return img

def extractDataFromReceipt(image_path):
    # Preprocess image
    img = preprocessImage(image_path)
    
    # OCR: Extract text using Hungarian language model
    custom_config = r'--oem 3 --psm 6 -l hun'
    raw_text = pytesseract.imageToString(img, config=custom_config)
    
    # Extract structured data (items, price, date)
    print("Raw OCR Output:\n", raw_text)

    # Extract bounding box and text for debugging (optional)
    d = pytesseract.imageToData(img, output_type=Output.DICT)
    
    # Loop through and extract item names, prices
    items = []
    prices = []
    date = None
    for i, text in enumerate(d['text']):
        if text.strip():  # Non-empty text
            if "Ft" in text:  # Assuming Hungarian prices in Forint (Ft)
                prices.append(text)
            elif any(char.isdigit() for char in text) and len(text.split('/')) == 3:
                date = text  # Assuming date format like 01/01/2024
            else:
                items.append(text)
    
    return items, prices, date

# Test the function with a sample receipt image
items, prices, date = extractDataFromReceipt('/home/pc52/myprojects/moneymaster/back/test/rec1.jpeg')

print("Items:", items)
print("Prices:", prices)
print("Date:", date)
