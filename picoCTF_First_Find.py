# Solution to picoCTF challenge First Find.

# Tags:
# 100 points
# picoGym Exclusive
# General skills

# Description: Unzip this archive and find the file named 'uber-secret.txt'.  Download zip file.

import requests
from zipfile import ZipFile
import re
import io

url = "https://artifacts.picoctf.net/c/551/files.zip"
filename = ''.join(re.findall("\w+\.\w+$", url))


print(f"Requesting data from {url}")
f = requests.get(url)

print(f"Opening {filename} using the zipfile module...")
with ZipFile(io.BytesIO(f.content)) as myzip:
    print(f"Reading every file within {filename} looking for the flag...")
    for filepath in myzip.namelist():
        with myzip.open(filepath) as text:
            flag = ''.join(re.findall("picoCTF{.*}", text.read().decode()))
            if flag:
                print(f"The flag was found in {filepath}")
                print(flag)
