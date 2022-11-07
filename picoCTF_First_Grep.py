# Solution to picoCTF challenge First Grep.

# Tags:
# 100 points
# picoCTF 2019
# General skills

# Description:
# Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

# Imports argv from sys module.
from sys import argv

# Imports the regular expressions module.
import re

# The script accepts a filename as an argument.
script, filename = argv

print(f"Opening '{filename}'...")
print("Looking for the flag using regular expressions... picoCTF{.*}")

# Opens the file.
with open(filename) as f:
    # Uses the regular expression to find the flag in the text.
    flag = re.findall("picoCTF{.*}", f.read())

# Prints the flag.
print("The flag is: " + ''.join(flag))
    

