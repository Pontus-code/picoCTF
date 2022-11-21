# Solution to picoCTF challenge Lets Warm Up.

# Tags:
# 50 points
# picoCTF 2021
# General skills

# Description:
# If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

print("Fist let's convert the hexadecimal (base16) '0x70' into decimal (base10).")
decimal = int("70", 16)
print(f"The hexadecimal '0x70' equals {decimal} in decimal.")

print(f"Now let's convert {decimal} into its corresponding ASCII character.")
character = chr(decimal)
print(f"{decimal} corresponds to the ASCII character '{character}'.")

print("The flag is picoCTF{" + character + "}")