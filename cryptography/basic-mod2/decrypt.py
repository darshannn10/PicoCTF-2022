#!/usr/bin/env python3 
import string

flag = []

with open("message.txt") as flip:
	contents = flip.read()
	numbers = [ int(val) for val in contents.split()]

	for num in numbers:
		mod = pow(num, -1, 41) # take modulus of each number
		print(mod)
		#putting each number in appropriate range
		if mod in range(1, 27):
			flag.append(string.ascii_uppercase[mod -1]) 
		elif mod in range(27, 37):
			flag.append(string.digits[mod - 27])
		else:
			flag.append("_")

#appending all the content together an printing the flag in picoctf style
print("picoCTF{%s}" % "".join(flag))