# Solution to picoCTF challenge vault-door-training.

# Tags:
# 50 points
# picoCTF 2019
# Reverse Engineering

# Description:
""" 
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. 
The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. 
Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, 
but one of our junior agents obtained the source code for each vault's computer! 
You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, 
we have created a replica vault in our training facility. The source code for the training vault is here: VaultDoorTraining.java
"""

# Imports the request library to handle HTTP requests.
import requests
# Imports the re library to handle regular expresssions. 
import re

# Address to source code file.
url = "https://jupiter.challenges.picoctf.org/static/1afdf83322ee9c0040f8e3a3c047e18b/VaultDoorTraining.java"
filename = ''.join(re.findall("\w*\.\w*$", url))

print(f"Downloading {filename}")
code = requests.get(url)
print(f"---BEGINNING OF SOURCE CODE---")
print(code.text)
print("---END OF SOURCE CODE---")
print("\nUsing regular expressions to find the flag...")
print("The flag is: picoCTF{" + ''.join(re.findall('(?<=equals\(")\w*', code.text)) + "}")