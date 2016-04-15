from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

"""
Just a wrapper for Crypto patterns for signing and verifying using public keys.
This is just a service object, since the code patterns it contains will be used often
"""
class Notary(object):
	def __init__(self):
		pass
a
	"""
	Hashes some data and signs it with a prv key.

	@data: Some raw string of bytes to hash and sign.
	@prvKeyPath: The path to some RSA-private key file; the Crypto libs use file names as their primary
	access point to keys.
	"""
	def Sign(self, data, prvKeyPath):
		if len(data) == 0:
			print("ERROR data empty, nothing to sign")
			return None

		key = RSA.importKey(open(prvKeyPath).read())
		h = SHA256.new()
		h.update(data)
		signer = PKCS1_v1_5.new(key)
		signature = signer.sign(h)
		print("signature: "+str(signature))

		return  signature
		
	def Verify(self, data, signature, pubKeyPath):
		key = RSA.importKey(open(pubKeyPath).read())
		h = SHA256.new(data)
		verifier = PKCS1_v1_5.new(key)
		if verifier.verify(h, signature):
			print("The signature is authentic.")
			return True	
		else:
			print("The signature is not authentic.")
			return False

