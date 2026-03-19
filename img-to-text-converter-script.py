pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # for setting path

import pytesseract
from PIL import Image

# Load image
img = Image.open("image.png")

# Extract text
text = pytesseract.image_to_string(img)

print(text)