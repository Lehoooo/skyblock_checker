# Made By Leho - github.com/Lehoooo
import re
print("Starting Username Extracter - Made By github.com/Lehoooo")

passwordfile = open("combo.txt", "r")
outputfile = open("usernames.txt", "w")
pass_split = passwordfile.read().split("\n")

for x in range(len(pass_split)):
    usernamesplit = re.split(f':|\n', pass_split[int(x)])
    outputfile.write(str(usernamesplit[2]) + "\n")
    print(usernamesplit[2])

outputfile.close()
passwordfile.close()

