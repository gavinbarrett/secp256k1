import unittest
from sys import path
path.append("..")
from secp256k1 import secp256k1

exp = (0xc6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5, 0x1ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a)

class TestPubKeyDerive(unittest.TestCase):
	def test_derive_1(self):
		pub_key = secp256k1().generate_pubkey(2)
		self.assertEqual(exp[0], pub_key.x)
		self.assertEqual(exp[1], pub_key.y)

if __name__ == "__main__":
	unittest.main()
