# Solution to picoCTF challenge extensions.

# Tags:
# 150 points
# picoCTF 2019
# Forensics

# Description:
# This is a really weird text file TXT? Can you find the flag?

# Try reading the file.
cat flag.txt

# Returns data that is not human readable. 
# Note the 'PNG' in the beginning of the file, part of a file signature.

file flag.txt
# Shows you that it's actually a PNG file, open in any image viewer app.

# The flag is: picoCTF{now_you_know_about_extensions} 
