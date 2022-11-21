# Solution to picoCTF challenge Glory of the Garden.

# Tags:
# 50 points
# picoCTF 2019
# Forensics

# Description: This garden contains more than it seems.
# Hint: What is a hex editor?

# URL to a file.
url = "https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg"

import re
import requests

filename = ''.join(re.findall("\w*\.\w*$", url))
print(f"Downloading {filename}")
file = requests.get(url)
print(f"Scanning {filename} for the flag...")
flag = re.findall("picoCTF{.*}", file.text)
print(''.join(flag))