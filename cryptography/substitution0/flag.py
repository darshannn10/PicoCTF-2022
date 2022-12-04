#!/usr/bin/env python3
import string

with open("message.txt") as flip:
    contents = flip.read()

uppercase_key = "VOUHMJLTESZCDKWIXNQYFAPGBR "
lowercase_key = uppercase_key.lower()

for character in contents:
    if character.isupper():
        position = uppercase_key.index(character)
        print(string.ascii_uppercase[position], end="")
    elif character.islower():
        position = lowercase_key.index(character)
        print(string.ascii_lowercase[position], end="")
    else:
        print(character, end="")