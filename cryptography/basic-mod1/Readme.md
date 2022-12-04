# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Cryptography |
| Challenge Name | Basic-mod1 |
| Points | 100 |

## Description

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})<br>
The message is:
```
202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397 
```

#### Hints

- Do you know what mod 37 means?
- mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Approach

```python
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
```

## Flag

```
picoCTF{R0UND_N_R0UND_79C18FB3}
```
