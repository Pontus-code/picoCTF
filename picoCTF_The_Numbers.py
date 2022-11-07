# Solution to picoCTF challenge The Numbers.

# Tags:
# 50 points
# picoCTF 2019
# Cryptography

# Description:
# The numbers... what do they mean?

# Imports the string module.
import string

# Adds the numbers and curly braces manually to a list.
numbers = ['16','9','3','15','3','20','6','{','20','8','5','14','21','13','2','5','18','19','13','1','19','15','14','}']

# Creates a string with the alphabet.
alphabet = string.ascii_lowercase

# Initializes and empty string
flag = ""

# For each entry in the list...
for n in numbers:
    # Try to convert it into an integer and add the corresponding character from the alphabet to the flag string.
    try:
        x = int(n)
        flag += alphabet[x-1]
    # If it cannot be converted into an integer, in this case a curly brace, add the original list item to the flag string.
    except:
        flag += n

flag_upper = ""
# Makes the CTF-part in picoCTF uppercase.
for i in range(len(flag)):
    if i>=4 and i<=6:
        flag_upper += flag[i].upper()
    else:
        flag_upper += flag[i]
   

# Prints the flag with proper capitalization.
print(flag_upper)
