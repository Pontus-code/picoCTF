# Solution to picoCTF challenge 2Warm.

# Tags:
# 50 points
# picoCTF 2019
# General skills

# Description: Can you convert the number 42 (base 10) to binary (base 2)?

# bin() to convert decimal to binary.
bin_42 = bin(42)
print(f"The decimal 42 is {bin_42} in binary.")
# bin_42[2:] removes the '0b' prefix from the binary string.
flag = "picoCTF{" + bin_42[2:] + "}"
print(f"The flag is: {flag}")