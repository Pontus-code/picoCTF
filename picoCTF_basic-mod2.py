import string

letters = list(string.ascii_lowercase + string.digits + "_")


with open("message.txt") as file:
	cipherstring = file.read()
	cipherlist = [int(i) for i in cipherstring.split()]
	inversemod = [pow(i, -1, 41) for i in cipherlist]	

	cleartext = ""
	for i in inversemod:
		x = letters[i - 1]
		cleartext += x

	print("picoCTF{" + cleartext + "}")
