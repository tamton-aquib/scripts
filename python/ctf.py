#!/usr/bin/env python3
from string import ascii_lowercase, ascii_uppercase
import sys

G, E = '\033[32m', '\033[0m'
d = { "A" :".-" , "B" :"-...", "C" :"-.-.", "D" :"-..", "E" :".", "F" :"..-.", "G" :"--.", "H" :"....", "I" :"..", "J" :".---", "K" :"-.-" , "L" :".-..", "M" :"--" , "N" :"-.", "O" :"---" , "P" :".--.", "Q" :"--.-" , "R" :".-.", "S"	:"...", "T" :"-", "U" :"..-" , "V" :"...-", "W" :".--", "X" :"-..-", "Y" :"-.--", "Z" :"--..", "0" :"-----", "1" :".----", "2" :"..---", "3" :"...--", "4" :"....-" , "5" :".....", "6" :"-....", "7" :"--...", "8" :"---..", "9" :"----.", "." :".-.-.-", "," :"--..--", "?" :"..--..", "=" :"-...-", ";" :"-.-.-.", ":" :"-...", "/" :"-..-.", "–" :"-....-", "'" :".-.", "”" :".-..-.", "+" :".-.-.", "*" :"-..-", "@" :".-.-.", } 
reverse_d = {v:k for k,v in d.items()}

def caesar(target):
	result = ""
	for i in range(26):
		noice = ""
		for c in target:
			if c in ascii_lowercase:
				noice += ascii_lowercase[(ascii_lowercase.index(c)+i) % 26]
			elif c in ascii_uppercase:
				noice += ascii_uppercase[(ascii_uppercase.index(c)+i) % 26]
			else:
				noice += c

			if "ctf" in noice.lower() or "flag" in noice.lower():
				noice = noice.replace(noice, f"{G}{noice}     <--{E}")

		result += f"[{str(i).zfill(2)}] : {noice}\n"
	
	return result

def morse(target):
	def morse_decode(s):
		decoded = ""
		for c in s.split():
			decoded += reverse_d.get(c, c)

		return decoded

	def morse_encode(s):
		encoded = ""
		for c in s:
			encoded += d.get(c.upper(), c) + " "

		return encoded

	if all([c in '-. ' for c in target]):
		return (morse_decode(target))
	else:
		return (morse_encode(target))

def log(s):  return (f'{s} not found!\nUsage: "python3 ctf.py (morse|rot) <string>"')

if __name__ == "__main__":
	if len(sys.argv) <= 2:
		print(log("Arguments"))
		sys.exit()

	type = sys.argv[1]
	query = sys.argv[2]

	print({ "rot": caesar, "caesar": caesar, "morse": morse }.get(type, log)(query))
