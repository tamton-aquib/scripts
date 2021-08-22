#!/usr/bin/env python3
import sys

d = {
	"A" :	".-" ,		
	"B" :	"-...",
	"C" :	"-.-.", 	
	"D" :	"-..",
	"E" :	".", 		
	"F" :	"..-.",
	"G" :	"--.", 	
	"H" :	"....",
	"I" :	"..", 		
	"J" :	".---",
	"K" :	"-.-" ,	
	"L" :	".-..",
	"M" :	"--" ,		
	"N" :	"-.",
	"O" :	"---" ,	
	"P" :	".--.",
	"Q" :	"--.-" ,	
	"R" :	".-.",
	"S"	:	"...", 	
	"T" :	"-",
	"U" :	"..-" ,	
	"V" :	"...-",
	"W" :	".--", 	
	"X" :	"-..-",
	"Y" :	"-.--", 	
	"Z" :	"--..",
	"0" :	"-----" ,	
	"1" :	".----",
	"2" :	"..---" ,	
	"3" :	"...--",
	"4" :	"....-" ,	
	"5" :	".....",
	"6" :	"-....", 	
	"7" :	"--...",
	"8" :	"---..", 	
	"9" :	"----.",
	"." :	".-.-.-", 	
	"," :	"--..--",
	"?" :	"..--..", 	
	"=" :	"-...-",
	";" : 	"-.-.-.",
	":" :	"-...",
	"/" :	"-..-.",
	"–" :	"-....-",
	"'" :	".-.",
	"”" :	".-..-.",
	"+" :	".-.-.",
	"*" :	"-..-",
	"@" :	".-.-.",
}

reverse_d = {v:k for k,v in d.items()}

if len(sys.argv) == 1:
	print('Usage: "python3 morse.py <morse_string>"')
	sys.exit()

string = sys.argv[1]

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

def main():
	if all([c not in '-. ' for c in string]):
		print(morse_encode(string))
	else:
		print(morse_decode(string))

if __name__ == '__main__':
	main()
