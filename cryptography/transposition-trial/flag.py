#!/usr/bin/env python3

with open("message.txt") as flip:
	contents = flip.read()

flag = []
for i in range(0, len(contents), 3):
	chunck = contents[i : i + 3]
	a, b, c = chunck
	flag.append(c+a+b)

if flag is not None:
	print(''.join(flag)).split()[-1]