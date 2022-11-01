# Solution to picoCTF challenge Bases.

# Tags:
# 100 points
# picoCTF 2019
# General skills

# Description:
# What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

import base64

base64_string = "bDNhcm5fdGgzX3IwcDM1"
base64_bytes = base64_string.encode("ascii")
decoded_bytes = base64.b64decode(base64_bytes)
decoded_string = decoded_bytes.decode("ascii")

print("The flag is: picoCTF{" + decoded_string + "}")
