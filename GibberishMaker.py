#!/usr/bin/python3
import random

print("""
  ____ _ _     _               _     _       __  __       _             
 / ___(_) |__ | |__   ___ _ __(_)___| |__   |  \/  | __ _| | _____ _ __ 
| |  _| | '_ \| '_ \ / _ \ '__| / __| '_ \  | |\/| |/ _` | |/ / _ \ '__|
| |_| | | |_) | |_) |  __/ |  | \__ \ | | | | |  | | (_| |   <  __/ |   
 \____|_|_.__/|_.__/ \___|_|  |_|___/_| |_| |_|  |_|\__,_|_|\_\___|_|   
			By Rentix Productions                                                                       

""")
print("\n")
print("Welcome to Gibberish Maker!")
print("How many lines of the gibberish would you like to get?")
try:
	lines = int(input("Lines: "))
except:
	print("Sorry. I don't understand uketerianburg..")
print("\n")
print("\n")
#print("Using regular char set because its the first version and fuck you")
#print("10 is max an min cause fuck you thats why")
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

final = ''
lis = []
for i in range(0, lines, 1):
	for i in range(0, 10):
		final += random.choice(chars)
	lis.append(final)
	final = ''

file = open('passwords.lst', 'w')
for line in lis:
	file.write(line)
	file.write('\n')
file.close()
print("DONE! Check your dir for passwords.lst")
