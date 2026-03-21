pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # for setting path

import pytesseract
from PIL import Image

# Load image
img = Image.open("image.png")

# Extract text
text = pytesseract.image_to_string(img)

print(text)

# for better accuracy 
import cv2
import pytesseract

# Set path if on Windows
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
img = cv2.imread("image.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# Remove noise
gray = cv2.medianBlur(gray, 3)

# OCR
text = pytesseract.image_to_string(gray)

print(text)

# also
text = pytesseract.image_to_string(gray, config="--psm 6")

# for saving to extrracted file
with open("output.txt", "w") as f:
    f.write(text)

if __name__ == "__main__":
    print("Text was generated successfully")
