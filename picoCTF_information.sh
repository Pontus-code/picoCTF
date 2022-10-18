#!/bin/bash

# picoCTF challenge information.

# Tags:
# 10 points
# picoCTF 2021
# Forensics

# Description:
# Files can always be changed in a secret way. Can you find the flag? cat.jpg

# Download the file.
wget https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg


# It's a picture file. Let's check it for metadata.
exiftool cat.jpg

# License: cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9. It looks base64 to me. Let's decode it.
echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d

# The flag is: picoCTF{the_m3tadata_1s_modified}
