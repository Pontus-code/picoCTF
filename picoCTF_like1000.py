# Solution of picoCTF challenge like1000.

# Tags:
# 250 points
# picoCTF 2019
# Forensics

# Description:
# This .tar file got tarred a lot...

# Download the file '1000.tar'.

# Imports the tarfile module.
import tarfile

# A for loop that counts backwards fom 1000.
for count in range (1000,0,-1):
    # Assigns a string with the filename, 1000.tar, 999.tar, 998.tar and so forth...
    filename = str(count) + '.tar'
    print(f"Opening {filename}...")
    t = tarfile.open(filename)
    print(f"Extracting {filename}...")
    t = t.extractall()

# Now that all the tars within tars are extracted, check out the flag.png file.
