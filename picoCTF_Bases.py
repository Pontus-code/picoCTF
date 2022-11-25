# Solution to picoCTF challenge Bases.

# Tags:
# 100 points
# picoCTF 2019
# General skills

# Description:
# What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

import base64

enc = "bDNhcm5fdGgzX3IwcDM1"

flag = base64.b64decode(enc).decode()

print("The flag is: picoCTF{" + flag + "}")
