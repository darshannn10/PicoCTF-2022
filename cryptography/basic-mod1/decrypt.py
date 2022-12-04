#!/usr/bin/env python3 
import string

flag = []

with open("message.txt") as flip:
	contents = flip.read() # read the contents
	numbers = [ int(val) for val in contents.split()]  # split the contents
	for num in numbers:
		mod = num % 37 # take modulus of each number
		
		#putting each number in appropriate range
		if mod in range(26):
			flag.append(string.ascii_uppercase[mod]) 
		elif mod in range(26, 36):
			flag.append(string.digits[mod - 26])
		else:
			flag.append("_")

#appending all the content together an printing the flag in picoctf style
print("picoCTF{%s}" % "".join(flag))