#!/usr/bin/env python3
from string import ascii_lowercase, ascii_uppercase
import sys

query = sys.argv[1]

G = '\033[32m'
E = '\033[0m'

def caesar(target):
	for i in range(26):
		noice = ""
		for c in target:
			if c in ascii_lowercase:
				noice += (ascii_lowercase[(ascii_lowercase.index(c)+i) % 26])
			elif c in ascii_uppercase:
				noice += (ascii_uppercase[(ascii_uppercase.index(c)+i) % 26])
			else:
				noice += c

			if "ctf" in noice.lower() or "flag" in noice.lower():
				noice = noice.replace(noice, f"{G}{noice}{E}")

		print(f"[{str(i).zfill(2)}] : {noice}")

caesar(query)
