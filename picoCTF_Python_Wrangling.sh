#!/bin/bash

# picoCTF challenge Python Wrangling.

# Tags:
# 10 points
# picoCTF 2021
# General skills


# Description:
# Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

# Download the python code.
wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py

# Download the password file.
wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/pw.txt

# read the password file
cat pw.txt

# Download the encoded flag.
wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/flag.txt.en

# Running the python script will reveal its usage 
python3 ende.py

# Usage: ende.py (-e/-d) [file]
# Assuming -e is for encoding and -d is for decoding we run the following line to decode our flag.
python3 -d flag.txt.en

# Provide the password from pw.txt: 192ee2db192ee2db192ee2db192ee2db

# The flag is: picoCTF{4p0110_1n_7h3_h0us3_192ee2db}


