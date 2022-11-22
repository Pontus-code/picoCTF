# Solution to picoCTF challenge Glory of the Garden.

# Tags:
# 50 points
# picoCTF 2019
# Forensics

# Description: This garden contains more than it seems.
# Hint: What is a hex editor?

import re
import requests
from PIL import Image



url = "https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg" # URL to a file.
filename = ''.join(re.findall('(\w*\.\w*$)', url)) # Regular expression to match the filename.

def showimage(): # Downloads and displays the image file in the default image viewer.
    print(f"Downloading {filename} from {url}...")
    response = requests.get(url, stream=True)
    print(f"Opening {filename} in the default image viewer...")
    img = Image.open(response.raw)
    img.show()


showimage()

print("No clue in the picture...")
file = requests.get(url)
print(f"Lets scan the {filename} file for the flag using regular expressions...")
flag = re.findall("picoCTF{.*}", file.text)
print(''.join(flag))
