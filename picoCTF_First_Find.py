# Solution to picoCTF challenge First Find.

# Tags:
# 100 points
# picoGym Exclusive
# General skills

# Description: Unzip this archive and find the file named 'uber-secret.txt'.  Download zip file.

import requests
from zipfile import ZipFile
import re
import os

url = "https://artifacts.picoctf.net/c/551/files.zip"
filename = ''.join(re.findall("\w+\.\w+$", url))


print(f"Requesting data from {url}")
f = requests.get(url)

print(f"Writing data to {filename}")
with open(filename, 'wb') as file:
    file.write(f.content)

print(f"Extracting all files from {filename}")
with ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall()

print(f"Opening all extracted files and searching for the picoCTF-flag using regular expressions...")
for root, dirs, files in os.walk('./files/', topdown=True):
    # Creating a file path for every file in every directory.
    for name in files:
        location = os.path.join(root + "/" + name)
    print(f"Searching {location}: ")
    with open(location) as txt:
        flag = ''.join(re.findall("picoCTF{.*}", txt.read()))
        if flag:
            flag_location = location

print(f"\nFlag location: {flag_location}")
print(f"The flag is: {flag}")