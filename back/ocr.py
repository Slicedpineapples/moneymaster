import cv2
import pytesseract
from pytesseract import Output

def preprocessImage(imagePath):
    # grasycale the image for better OCR accuracy
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    
    # Resize image to improve OCR accuracy
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    # Apply GaussianBlur to reduce noise 
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # Apply thresholding to binarize the image
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
    #save the preprocessed image for debugging
    #cv2.imwrite('/home/pc52/myprojects/moneymaster/back/test/preprocessed_image.jpeg', img)
    return img

def extractDataFromReceipt(imagePath):
    # Preprocess image
    img = preprocessImage(imagePath)
    
    # OCR: Extract text using Hungarian language model
    customConfig = r'--oem 3 --psm 6 -l hun'
    rawText = pytesseract.image_to_string(img, config=customConfig)
    
    # Extract structured data (items, price, date)
    print("Raw OCR Output:\n", rawText)

    # Split the text into lines
    lines = rawText.split('\n')
    return rawText

# Test the function with a sample receipt image
extractDataFromReceipt('/home/pc52/myprojects/moneymaster/back/test/rec1.jpeg')



