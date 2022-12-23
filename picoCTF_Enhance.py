# Solution to picoCTF challenge Enhance!

# Tags:
# 100 points
# picoCTF 2022
# Forensics

# Descriptions: Download this image file and find the flag.

import requests
import re

URL = "https://artifacts.picoctf.net/c/137/drawing.flag.svg"

file = requests.get(URL)

print("Lets have a look at the file.")
print("-" * 20)
print(file.text)
print("-" * 20)

print("There is something interesting happening between id=\"tspanXXXX\"> and </tspan>")
flag_parts = re.findall("id=\"tspan\d{4}\">(.+)</tspan>",file.text)
print("Regular expressions matches the following:\n" + str(flag_parts))
flag = ''.join(flag_parts).replace(" ", "")

print("The flag is: " + flag)
