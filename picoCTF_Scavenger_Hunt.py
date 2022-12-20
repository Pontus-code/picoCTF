# Solution to picoCTF challenge Scavenger Hunt.

# Tags:
# 50 points
# picoCTF 2021
# Web exploitation

# Description: 
# There is some interesting information hidden 
# around this site http://mercury.picoctf.net:5080/. 
# Can you find it?

import requests
import re
from bs4 import BeautifulSoup

url = "http://mercury.picoctf.net:5080/"

# Sends a GET request to the url and parse the HTML for files with BeautifulSoup.
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# List of files 
files = []
# Creates an empty list for flag parts.
parts = []

# Adds som interesting files to the list.
for file in ['index.html', 'robots.txt', '.htaccess', '.DS_Store']:
    files.append(url + file)

# Finds any CSS files and adds them to the list.
for css in soup.find_all("link"):
	if css.attrs.get("href"):
		css_url = css.attrs.get("href")
		files.append(url + css_url)

# Finds any JavaScript files and adds them to the list.
for script in soup.find_all("script"):
	if script.attrs.get("src"):
		script_url = script.attrs.get("src")
		files.append(url + script_url)

# Requests all files in list and scans them for flag part using regular expressions.
def scan(files):
	for file in files:
		print("")
		print(f"Found the following file: {file}")
		filename = ''.join(re.findall("\w*\.\w*$", file))
		print(f"Downloading {filename}")
		response = requests.get(file)
		print(response)
		if response.status_code != 404:
			print("Scanning for flag...")
			hint = re.findall(".*flag.*|.*part.*|\/\*.*\/*/|.*Part.*", response.text)
			if hint:
				print(f"Matched this line(s): {' '.join(hint)}")
				part = re.findall("(?<=: )[A-Za-z0-9_}{]+", str(hint))
				print(f"Matched this flag part: {''.join(part)}")
				parts.append(''.join(part))
			else:
				print("No hint found...")
		else:
			print("Download failed...")

scan(files)

# Arranges the flag parts.
flag = ''.join([parts[i] for i in (0,4,1,2,3)])

print("\nThe complete flag is: " + flag)
