# Solution to picoCTF challenge extensions.

# Tags:
# 150 points
# picoCTF 2019
# Forensics

# Description:
# This is a really weird text file TXT? Can you find the flag?

# Requests library handles HTTP-requests.
import requests
# Pillow library handles images.
from PIL import Image
# re library handles regular expressions.
import re
# Pytesseract library handles optical character recognition (OCR).
# Make sure you have tesseract installed on your system.
import pytesseract


# URL to file.
url = "https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt"
# Name of the file.
filename = ''.join(re.findall('(\w*\.\w*$)', url))

# Prints the beginning of the file.
def printfile():
    print(f"Downloading {filename}")
    response = requests.get(url, stream=True)
    print(f"Printing the first 100 characters of {filename}...\n")
    print(response.text[:100])
    print("\nThis is not a text file! PNG is a file signature suggesting its an image file.")

# Opens the file in the default image viewer.
def openimage():
    print(f"\nOpening {filename} in your image viewer...")
    response = requests.get(url, stream = True)
    img = Image.open(response.raw)
    img.show()
    
# Converts image to text.
def imagetotext():
    print(f"\nReading text from image using OCR on {filename}...")
    try: 
        response = requests.get(url, stream = True)
        img = Image.open(response.raw)
        text = pytesseract.image_to_string(img)
        print(text)
    except:
        print("Couldn't make image to text conversion, maybe tesseract is not installed on your system...")

while True:
    print(f"""
    What do you want to do with {filename}?
    0) Print the contents of {filename}
    1) Open {filename} in an image viewer.
    2) Scan {filename} using Optical Character Recocgnition.
    3) Exit
    """)
    option = ''
    try:
        option = int(input("=> "))
    finally:
        if option == 0:
            printfile()
            continue
        if option == 1:
            openimage()
            continue
        if option == 2:
            imagetotext()
            continue
        if option == 3:
            print("Exiting program")
            break
        else:
            print("Invalid option, try again...")
            continue
