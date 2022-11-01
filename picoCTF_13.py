# Solution to picoCTF challenge 13.

# Tags:
# 100 points.
# picoCTF 2019
# Cryptography

# Description:
# Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

import string

cleartext = ""
cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
alphabet = string.ascii_lowercase

# Iterate throught the cipher string.
for c in cipher:
    # Makes the character lower case.
    d = c.lower()
    # Finds the position of the character in the alphabet.
    index = alphabet.find(d)
    # If the character is not in the alphabet, it will return a position of -1.
    if index == -1:
        # Add the character to the cleartext string as it is.
        cleartext = cleartext + c
    else:
        # Rotate the position of the character 13 times and start over from the beginning if exceeding the number of characters in the alphabet string.
        new_index = (index + 13) % len(alphabet)
        # Assigns the letter of the alphabet after rotation.
        deciphered = alphabet[new_index]
        # If the original character was uppercase, make the deciphered character uppercase.
        if c.isupper():
            deciphered = deciphered.upper()
        # Add the deciphered character to the cleartext string.
        cleartext = cleartext + deciphered
 
print(f"The flag is: {cleartext}")
