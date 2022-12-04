# picoCTF 2022

> Darshan Patel

## Overview

| Tables | Description |
| ------ | ----------- |
| Category | Cryptography |
| Challenge Name | Basic-mod2 |
| Points | 100 |

## Description

A new modular challenge!
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message}) <br><br>
The message is: 
```
104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377 
```

#### Hints

- Do you know what the modular inverse is?
- The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
- It's recommended to use a tool to find the modular inverses

## Approach

```python
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
```

## Flag

```
picoCTF{1NV3R53LY_H4RD_C680BDC1}
```
