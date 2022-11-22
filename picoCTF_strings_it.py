# Solution to picoCTF challenge strings it.

# Tags:
# 100 points
# picoCTF 2019
# General skills

# Description: Can you find the flag in file without running it?

import requests # Handles HTTP requests.
import re       # Handles regular expressions.

url = "https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings"
filename = ''.join(re.findall("\w*$", url))

print(f"Downloading {filename} from {url}...")
response = requests.get(url)
print("Scanning the file contents for the flag with regular expression...")
flag = ''.join(re.findall("picoCTF{.*}", response.text))
print("The flag is: " + flag)