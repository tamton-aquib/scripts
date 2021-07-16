#!/usr/bin/env python3
import hashlib, pikepdf, zipfile
import sys, time

R, G, B, E = "\033[31m", "\033[32m", "\033[36m", "\033[0m"

def ettup():
	for passwd in passlist:
		try:
			with pikepdf.open(filename, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print(f"{G}--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				sys.exit()

		except pikepdf._qpdf.PasswordError:
			print(f"{R}trying: {passwd}")

def ettuh():
	for line in lines:
		enc_wrd = line.encode()
		if len(filename) == 64:
			digest = hashlib.sha256(enc_wrd).hexdigest().lower()
		elif len(filename) == 32:
			digest = hashlib.md5(enc_wrd).hexdigest().lower()
		elif len(filename) == 128:
			digest = hashlib.sha512(enc_wrd).hexdigest().lower()
		elif len(filename) == 40:
			digest = hashlib.sha1(enc_wrd).hexdigest().lower()
		elif len(filename) == 96:
			digest = hashlib.sha384(enc_wrd).hexdigest().lower()
		elif len(filename) == 56:
			digest = hashlib.sha224(enc_wrd).hexdigest().lower()
		else:
			print("Meh")
			break

		if digest == filename:
			print(f"{G}---------------------------------------------------")
			print(f"         Password Found! --> {line}               ")
			print(f"---------------------------------------------------{E}")
			break
		else:
			print(f"{R}trying : {line}")

def ettuz():
	for password in lines:
		try:
			with zipfile.ZipFile(file=filename) as my_zip:
				my_zip.extractall('extracted',pwd=bytes(password.encode('utf-8').strip()))
				print(f"{G}-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				break
		except:
			print(f'{R}trying: ' + password)
			time.sleep(0.0001)

if len(sys.argv) <= 3:
	print("Usage: ettuh.py (zip|hash|pdf) filename/hash dictionary")
	sys.exit()

filename = sys.argv[2]
passlist = sys.argv[3]
option = sys.argv[1]

with open(passlist,'r') as f:
	lines = [password for password in f.read().split('\n') if password]

if option == 'zip':
	ettuz()
elif option == 'pdf':
	ettup()
elif option == 'hash':
	ettuh()
else:
	print("GTFO!")
