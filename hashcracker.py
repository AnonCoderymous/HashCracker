#!/usr/bin/python

import hashlib
import functions
import os
from datetime import datetime

global i
global count

count=0
i=0
lists = []
print("\n")
print("HASH CRACKER")
print("\n")
print("FOLLOWING HASH TYPES AVAILABLE: ")
print("1) sha3_512")
print("2) sha256")
print("3) sha384")
print("4) sha512")
print("5) sha224")
print("6) sha3_256")
print("7) sha1")
print("8) sha3_384")
print("9) blake2b")
print("10) blake2s")
print("11) sha3_224")
print("12) shake_128")
print("13) shake_256")
print("14) md5")
checkInput = int(input("Enter hash you want to crack: "))
hashInput = input("Enter hash to crack: ")
file = input("Enter path of wordlist file path (leave empty for default ): ")
if len(file) == 0 or file == "":
	file = "wordlist.txt"

if not os.path.exists(file):
	print("File does not exist !")
	exit(0)
else:
	with open(file, "r", encoding="UTF=8") as f:
		content = f.readlines()
		f.close()
for word in content:
	if(checkInput==1):
		if functions.sha3_512(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==2):
		if functions.sha256(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==3):
		if functions.sha384(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==4):
		if functions.sha512(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==5):
		if functions.sha224(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==6):
		if functions.sha3_256(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==7):
		if functions.sha1(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==8):
		if functions.sha3_384(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==9):
		if functions.blake2b(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==10):
		if functions.blake2s(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==11):
		if functions.sha3_224(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==12):
		if functions.shake_128(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==13):
		if functions.shake_256(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	if(checkInput==14):
		if functions.md5(word[:-1]) == hashInput:
			print("HASH CRACKED at {}".format(datetime.now()))
			print("\n")
			print("Plain Text: {}".format(word))
			break
		else:
			continue
	else:
		print("Invalid Hash Type Selected !")
		break