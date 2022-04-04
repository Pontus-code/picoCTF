import string

letters = list(string.ascii_uppercase + string.digits + "_")

with open("message.txt") as file:
        cipher = file.read()
        numbers = [int(i) for i in cipher.split()]
        modnumbers = [i % 37 for i in numbers]
        cleartext = ""
        for i in modnumbers:
                x = letters[i]
                cleartext = cleartext + x
        
print("picoCTF{" + cleartext +"}")
