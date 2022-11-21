# Solution to picoCTF challenge Insp3ct0r.

# Tags:
# 50 points
# picoCTF 2019
# Web Exploitation

# Description:
# Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ (link) or http://jupiter.challenges.picoctf.org:41511 

# Imports requests library to handle HTTP requests.
import requests
# Imports the BeautifulSoup library to handle HTTP data.
from bs4 import BeautifulSoup
# Imports re library to match flag parts using regular expressions.
import re


url = "http://jupiter.challenges.picoctf.org:41511"

# Creates an empty list for flag parts.
parts = []

# Sends a GET request to the url.
response = requests.get(url)

print("\nScanning the HTML source code for flag parts...")
hint = re.findall(".*flag.*", response.text)
print(f"Matched this line: {''.join(hint).strip()}")
part = re.findall("(?<=flag: )\S*", str(hint))
print(f"Matched this flag part: {''.join(part)}")
parts.append(part)

soup = BeautifulSoup(response.text, "lxml")

js_files = []
css_files = []

# Finds any JavaScript files and adds them to the list.
for script in soup.find_all("script"):
	if script.attrs.get("src"):
		script_url = script.attrs.get("src")
		js_files.append(url + "/" + script_url)

# Finds any CSS files and adds them to the list.
for css in soup.find_all("link"):
	if css.attrs.get("href"):
		css_url = css.attrs.get("href")
		css_files.append(url + "/" + css_url)

# Request each JavaScript file and scans for flag parts with regular expression.		
for file in js_files:
	print(f"\nFound the following JavaScript file: {file}")
	filename = ''.join(re.findall("\w*\.\w*$", file))
	print(f"Downloading {filename}")
	response = requests.get(file)
	print(response)
	print("Scanning for flag...")
	hint = re.findall(".*flag.*", response.text)
	if hint:
		print(f"Matched this line: {''.join(hint).strip()}")
		part = re.findall("(?<=flag: )\S*", str(hint))
		print(f"Matched this flag part: {''.join(part)}")
		parts.append(part)
	else:
		print("No flag found...")

# Requests all CSS files and scans them for flag part using regular expressions.
for file in css_files:
	print("")
	print(f"Found the following CSS file: {file}")
	filename = ''.join(re.findall("\w*\.\w*$", file))
	print(f"Downloading {filename}")
	response = requests.get(file)
	print(response)
	if response.status_code != 404:
		print("Scanning for flag...")
		hint = re.findall(".*flag.*", response.text)
		if hint:
			print(f"Matched this line: {''.join(hint).strip()}")
			part = re.findall("(?<=flag: )\S*", str(hint))
			print(f"Matched this flag part: {''.join(part)}")
			parts.append(part)
		else:
			print("No flag found...")
	else:
		print("Download failed...")

# Prints the flag parts in order.
print(f"\nFlag part 1/3 is {''.join(parts[0])}")
print(f"Flag part 2/3 is {''.join(parts[2])}")
print(f"Flag part 3/3 is {''.join(parts[1])}")

# Prints the whole flag from its parts.
print("\nThe flag is ", end = '')
for part in [0,2,1]:
	print(''.join(parts[part]), end = '')
print("")




