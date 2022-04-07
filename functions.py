import hashlib

def blake2s(string):
	result = hashlib.blake2s(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha3_384(string):
	result = hashlib.sha3_384(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha3_256(string):
	result = hashlib.sha3_256(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha3_224(string):
	result = hashlib.sha3_224(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha512(string):
	result = hashlib.sha512(string.encode())
	hashed = result.hexdigest()
	return hashed

def blake2b(string):
	result = hashlib.blake2b(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha3_512(string):
	result = hashlib.sha3_512(string.encode())
	hashed = result.hexdigest()
	return hashed

def md5(string):
	result = hashlib.md5(string.encode())
	hashed = result.hexdigest()
	return hashed

def blake2s(string):
	result = hashlib.blake2s(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha224(string):
	result = hashlib.sha224(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha3_256(string):
	result = hashlib.sha3_256(string.encode())
	hashed = result.hexdigest()
	return hashed

def shake_128(string):
	result = hashlib.shake_128(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha384(string):
	result = hashlib.sha384(string.encode())
	hashed = result.hexdigest()
	return hashed

def shake_256(string):
	result = hashlib.shake_256(string.encode())
	hashed = result.hexdigest()
	return hashed

def sha1(string):
	result = hashlib.sha1(string.encode())
	hashed = result.hexdigest()
	return hashed