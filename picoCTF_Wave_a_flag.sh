#!/bin/bash

# picoCTF challenge Wave a flag.

# Tags:
# 10 points
# picoCTF 2021
# General skills

# Description:
# Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

# Download the binary.
wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm

# Make it executable.
chmod +x warm

# Run it.
./warm

# Hello user! Pass me a -h to learn what I can do!
./warm -h

# Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}




