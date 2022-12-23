# Solution to picoCTF challenge Lookey here.

# Tags:
# 100 points
# picoCTF 2022
# Forensics

# Description: 
# Attackers have hidden information in a very large mass of 
# data in the past, maybe they are still doing it.
# Download the data here.'

import requests
import re

URL = "https://artifacts.picoctf.net/c/295/anthem.flag.txt"

file = requests.get(URL)

flag = ''.join(re.findall("picoCTF{.*}", file.text))

print(flag)