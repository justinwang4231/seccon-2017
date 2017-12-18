import pytest
from random import randint
from speck import SpeckCipher
from simon import SimonCipher
import binascii
def test_speck64_96(keyi):
	key=binascii.hexlify(keyi)
	print key
	key=int("0x"+key,16)
        plaintxt = 0x6d564d37426e6e71
        ciphertxt = 0xbb5d12ba422834b5
        block_size = 64
        key_size = 96
        c = SimonCipher(key, key_size, block_size, 'ECB')
	print hex(c.encrypt(plaintxt))
        if c.encrypt(plaintxt) == ciphertxt:
		print keyi
        if c.decrypt(ciphertxt) == plaintxt:
		print keyi
for a in range(32,128):
	print a
	for b in range(32,128):
		for c in range(32,128):
			for d in range(32,128):
				pass
test_speck64_96("SECCON{6Pz0}")
