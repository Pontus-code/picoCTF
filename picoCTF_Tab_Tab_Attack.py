# Solution to picoCTF challenge Tab, Tab, Attack.

# Tags:
# 20 points
# picoCTF 2021
# General skills

# Description: 
# Using tabcomplete in the Terminal will add years to your life, 
# esp. when dealing with long rambling directory structures and filenames: 
# Addadshashanammu.zip

import requests
from zipfile import ZipFile
import re
import io

URL = "https://mercury.picoctf.net/static/72712e82413e78cc8aa8d553ffea42b0/Addadshashanammu.zip"
filename = ''.join(re.findall("\w+.\w+$", URL))

print(f"Downloading {filename} using the requests module...")
f = requests.get(URL)
print(f"Opening {filename} using the zipfile module...")
with ZipFile(io.BytesIO(f.content)) as myzip:
    print(f"Reading every file within {filename}\nLooking for the flag using the re module...")
    for filepath in myzip.namelist():
        if myzip.read(filepath): # Only files, directories has no data.
            file = myzip.read(filepath).decode(errors="replace")
            flag = ''.join(re.findall("picoCTF{.*}", file))
            print("The flag was found in:\n" + filepath)
            print("The flag is " + flag)
