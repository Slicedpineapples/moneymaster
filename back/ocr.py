import cv2
import pytesseract
from pytesseract import Output
import re
import json

def preprocessImage(imagePath):

    filename = 'preprocessed'+imagePath.split('/')[-1]
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE) # grasycale the image for better OCR accuracy
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)  # Resize image to improve OCR accuracy
    img = cv2.GaussianBlur(img, (1, 1), 90)     # Apply GaussianBlur to reduce noise 
    # _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)     # Apply thresholding to binarize the image

    #save the preprocessed image for debugging
    cv2.imwrite(f'/home/pc52/myprojects/moneymaster/back/test/{filename}', img)
    return img

def extractDataFromReceipt(imagePath):
    # Preprocess image
    img = preprocessImage(imagePath)
    
    # OCR: Extract text using Hungarian language model
    customConfig = r'--oem 3 --psm 6 -l hun'
    rawText = pytesseract.image_to_string(img, config=customConfig)
    
    # Extract structured data (items, price, date)
    # print("Raw OCR Output:\n", rawText)

    # Split the text into lines
    lines = rawText.split('\n')
    return rawText

# Extract the merchant name
def extract_merchant_name(text):
    # Assuming merchant name is usually the first line in the receipt accoding to ISO 3166-1 alpha-2
    lines = text.splitlines()
    for line in lines:
        if re.search(r'\bKFT\b', line, re.IGNORECASE):
            return line.strip()
    return lines[0] if lines else None

# Extract receipt Date
def extract_receipt_date(text):
    # Look for the total cost line which usually contains "ÖSSZESEN"
    match = re.search(r'(\d{4}\.\d{2}\.\d{2})', text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


# Extract items and prices
def extract_items_prices(extractedData):
    # Split the extracted data into lines
    lines = extractedData.split('\n')

    # Initialize the dictionary to store items and prices
    items_dict = {}

    # Regular expression to capture prices (whole numbers before the decimal point)
    price_pattern = r'(\d{1,3}(?:\.\d{3})?|\d+)\s?[€]?[Ft]?'  # Matches prices like 199, 499, etc.

    # Loop through the lines to extract items and avoid unnecessary text
    inside_item_section = False

    for i in range(len(lines)):
        line = lines[i].strip()

        # Check for the start of the items section (after NYUGTA)
        if 'NYUGTA' in line:
            inside_item_section = True
            continue

        # Check for the end of the items section (before ÖSSZESEN)
        if 'ÖSSZESEN' in line:
            inside_item_section = False
            continue

        # Skip lines that contain "RÉSZÖSSZEG"
        if 'RÉSZÖSSZEG' in line:
            continue

        # Extract items and their prices within the items section
        if inside_item_section and line:
            # Try to find a price using the regular expression
            price_match = re.search(price_pattern, line)
            
            if price_match:
                # Extract the price (only the whole number part)
                price = price_match.group(1).replace(',', '').replace('.', '')

                # Extract the item name (everything before the price)
                item_name = line[:price_match.start()].strip()

                # Store item and price in dictionary
                items_dict[item_name] = int(price)

    # Organize the data into a dictionary
    receipt_data = {
 
        "items": items_dict
    }

    # Convert the dictionary to a JSON object
    receipt_json = json.dumps(receipt_data, indent=4, ensure_ascii=False)
    return receipt_json

# merch = extract_merchant_name(extractDataFromReceipt('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg'))
# print(merch)

# recDate = extract_receipt_date(extractDataFromReceipt('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg'))
# print(recDate)

# print(extractDataFromReceipt('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg'))

print(extract_items_prices(extractDataFromReceipt('/home/pc52/myprojects/moneymaster/back/test/rec4.jpeg')))