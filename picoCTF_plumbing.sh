# Solution to picoCTF challenge plumbing.

# Tags:
# 200 points
# picoCTF 2019
# General skills

# Description:
# Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

# Connecting with netcat return a huge amount of text, lets pipe the output to grep.
nc jupiter.challenges.picoctf.org 7480 | grep picoCTF

# The flag is: picoCTF{digital_plumb3r_06e9d954}
