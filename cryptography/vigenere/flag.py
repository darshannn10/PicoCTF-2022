#!/usr/bin/env python3

import string

ciphertext = b"rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"
key = "CYLAB"

def vigenere(plaintext, key):

    plaintext = plaintext.upper()
    key = bytes(key.upper(), "ascii")

    valid_chars = bytes(string.ascii_uppercase, "ascii")

    idx = 0
    ciphertext = ""

    for c in plaintext:
        if c not in valid_chars:
            ciphertext += chr(c)
        else:
            if key[idx] not in valid_chars:
                idx = (idx + 1) % len(key)
            # v1 = ord(c) - ord('A')
            # v2 = ord(key[idx]) - ord('A')
            v1 = c - ord("A")
            v2 = key[idx] - ord("A")
            ciphertext += chr(((v1 - v2) % 26) + ord("A"))
            idx = (idx + 1) % len(key)

    return ciphertext

print(vigenere(ciphertext, key))