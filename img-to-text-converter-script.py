import pytesseract
from PIL import Image

# Load image
img = Image.open("image.png")

# Extract text
text = pytesseract.image_to_string(img)

print(text)