#!/bin/bash

# picoCTF challenge Mod 26.

# Tags:
# 10 points.
# picoCTF 2021
# Cryptography

# Description:
# Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}

# Assigns the ciphertext to a variable.
ciphertext="cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"

# Text replacement that will shift characters 13 steps.
rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"

# Pipe the ciphertext to the rot13 text replacement function.
echo $ciphertext | $rot13

# The flag is: picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}
