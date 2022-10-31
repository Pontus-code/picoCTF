# picoCTF challenge Nice netcat...

# Tags:
# 15 points
# picoCTF 2021
# General skills

# Description:
# There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449, but it doesn't speak English...

# Connect and you will receive numbers. Output them to a file.
# nc mercury.picoctf.net 7449 > numbers.txt

# We have text file with numbers, one number for each row. 
# We assume each number represent an ASCII character. 
# Let's write a python script to convert the numbers into characters!

# Opens the file and reads its contents to a string variable.
with open(numbers.txt) as f:
    contents = f.read()

# Separates the numbers and assigns them to a list of strins.
list = contents.split('\n')

# The last entry in the list is an empty string. It  will cause an error when being converted into an integer later.
# Removes the empty string from the list.
list.remove('')

# Converts every entry in the list from a string to an integer, then converts the integer into it's corresponding ASCII character and prints the results.
for number in list:
    print(chr(int(number)))

# The flag is: picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
