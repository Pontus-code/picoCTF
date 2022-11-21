# Solution to picoCTF challenge Warmed Up.

# Tags:
# 50 points
# picCTF 2019
# General Skills

# Description: What is 0x3D (base 16) in decimal (base 10)?

hex = "3D"
dec = int("3D", 16)
char = chr(dec)
flag = "picoCTF{" + str(dec) + "}"

print(f"The hexadecimal {hex} is {dec} in decimal which corresponds to the character '{char}' in ASCII.")
print(f"The flag is: {flag}")