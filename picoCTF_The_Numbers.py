# Solution to picoCTF challenge The Numbers.

# Tags:
# 50 points
# picoCTF 2019
# Cryptography

# Description:
# The numbers... what do they mean?

import string           # Imports the string library,
import requests         # Requests library handles HTTP requests.
from PIL import Image   # Python Image Library handles images.
import re               # re library handles regular expressions.


url = "https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png" # URL to the image file.
filename = ''.join(re.findall('(\w*\.\w*$)', url)) # Regular expression to match the filename.

# Adds the numbers and curly braces manually to a list. I tried OCR with pytesseract unsuccessfully.
numbers = ['16','9','3','15','3','20','6','{','20','8','5','14','21','13','2','5','18','19','13','1','19','15','14','}']


def showimage(): # Downloads and displays the image file in the default image viewer.
    print(f"Downloading {filename} from {url}...")
    response = requests.get(url, stream=True)
    print(f"Opening {filename} in the default image viewer...")
    img = Image.open(response.raw)
    img.show()


def decipher(numbers): # Converts the numbers to corresponding position in the alphabet. 1 => a and 2 => b and so forth.
    flag = '' # Initializes and empty flag string.
    count = 0 # Initializes a counter to keep track of the position in the flag.
    for n in numbers:
        count += 1
        try: # Try to convert it into an integer and add the corresponding character from the alphabet to the flag string.
            x = int(n)
            if (count >=5 and count <= 7): # If flag position 5-7, make it uppercase as in 'picoCTF'
                flag += string.ascii_uppercase[x-1]
            else:
                flag += string.ascii_lowercase[x-1]
        except: # If it cannot be converted into an integer, in this case its a curly brace, add the original item to the flag string.
            flag += n
    return flag # return the flag as the functions output.
         

showimage()
print(f"The image displays the following characters: {' '.join(numbers)}")
print(f"Converting the numbers to their corresponding position in the alphabet: {decipher(numbers)}")
