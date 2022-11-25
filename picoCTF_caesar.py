# Solution to picoCTF challenge caesar.

# Tags:
# 100 points
# picoCTF 2019
# Cryptography

# Description:
# Decrypt this message (picoCTF{dspttjohuifsvcjdpoabrkttds})

import string

cipher = "dspttjohuifsvcjdpoabrkttds"
# Assigns a string with the alphabet in lowercase.
alphabet = string.ascii_lowercase

# Iterates through all possible rotations, 1-25.
for rotation in range(1, len(alphabet)):
    cleartext = ""
    for c in cipher:
        # Finds the characters position in the alphabet.
        index = alphabet.find(c)
        # Adds the rotation number to the position and loops it around if over 26.
        new_index = (index + rotation) % len(alphabet)
        # Assigns the deciphered character.
        deciphered = alphabet[new_index]
        cleartext += deciphered
    # Ends each nested loop with printing the possible flag.
    print("Rotation of " + str(rotation) + " gives the possible flag: picoCTF{" + cleartext + "}")
   
