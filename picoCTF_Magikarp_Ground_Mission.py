# Solution to picoCTF challenge Magikarp Ground Mission.

# Tags:
# 30 points
# picoCTF 2021
# General skills

# Description:
# Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

# For this challenge to work it has to be activated on the website first by pressing "Launch Instance"
# Make sure you use the correct port number.

# Imports the paramiko module for handling SSH connections.
import paramiko

host = "venus.picoctf.net" # Dont forget to "launch instance".
port = 52933 # Changes between instances.
username = "ctf-player"
password = "ee388b88"

# This function establishes an SSH connection and sends a command.
def ssh_command(host, port, username, password, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port = port, username = username, password = password)
    stdin, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print(f"'{cmd}' returns the following output:")
        print(''.join(output))
    else:
        print("No output, something went wrong...")


# A dictionary of commands and comments.
inputs =   {'ls': 'Lets start by listing the files in the working directory...', 
            'find / -name "[1-3]of3.flag.txt" 2>/dev/null': 'Now lets find the other parts of the flag...',
            'cat /home/ctf-player/drop-in/1of3.flag.txt': 'Reading the first part of the flag...',
            'cat /2of3.flag.txt': 'Reading the second part of the flag...',
            'cat /home/ctf-player/3of3.flag.txt': 'Reading the third part of the flag...',
            'cat /home/ctf-player/drop-in/1of3.flag.txt /2of3.flag.txt /home/ctf-player/3of3.flag.txt | tr "\\n" " "': 'The complete flag is...'}

def flag():
    for command in inputs:
        print(inputs[command])
        ssh_command(host, port, username, password, command)
    
def user():
    cmd = input(f"What command do you want to send to {host}:{port}? ")
    ssh_command(host, port, username, password, cmd)


while True:
    print("Choose 0 to send a custom command to the server")
    print("Choose 1 to initilize the flag finding script")
    print("Choose 2 to exit.")
    option = ''
    try:
        option = int(input("=> "))
    finally:
        if option == 0:
            user()
            continue
        if option == 1:
            flag()
            continue
        if option == 2:
            print("Exiting...")
            break
        else:
            print("Invalid options. Try again...")
            continue


