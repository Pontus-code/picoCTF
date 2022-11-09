# Solution to picoCTF challenge Magikarp Ground Mission.

# Tags:
# 30 points
# picoCTF 2021
# General skills

# Description:
# Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

# Connect from the terminal.
# ssh ctf-player@venus.picoctf.net -p 51595
# Provide the password 'ee38b88'

# List the contents of the current directory.
ls

# This will show you a file '3of3.flag.txt'.

# Assuming the other files with parts of the flag have similar names...
find / -name "*flag.txt* 2>/dev/null

# This will return three files, cat them and stitch them together.
cat /home/ctf-player/3of3.flag.txt
cat /home/ctf-player/drop-in/1of3.flag.txt
cat /2of3.flag.txt 


# The flag is: picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}


