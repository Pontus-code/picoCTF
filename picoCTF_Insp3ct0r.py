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


# Sends a GET request to the url and parse the HTML for files with BeautifulSoup.
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# List of files 
files = []
# Creates an empty list for flag parts.
parts = []

# Adds the HTML file to the list.
files.append((url + "/index.html"))

# Finds any CSS files and adds them to the list.
for css in soup.find_all("link"):
	if css.attrs.get("href"):
		css_url = css.attrs.get("href")
		files.append(url + "/" + css_url)

# Finds any JavaScript files and adds them to the list.
for script in soup.find_all("script"):
	if script.attrs.get("src"):
		script_url = script.attrs.get("src")
		files.append(url + "/" + script_url)


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
			hint = re.findall(".*flag.*", response.text)
			if hint:
				print(f"Matched this line: {''.join(hint).strip()}")
				part = re.findall("(?<=flag: )\S*", str(hint))
				print(f"Matched this flag part: {''.join(part)}")
				parts.append(''.join(part))
			else:
				print("No flag found...")
		else:
			print("Download failed...")

scan(files)

# Prints the whole flag from its parts.
print("\nThe complete flag is: " + ''.join(parts))




