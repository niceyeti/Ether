from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import rsa

"""
Just a wrapper for Crypto patterns for signing and verifying using public keys.
This is just a service object, since the code patterns it contains will be used often.
It just implements both directions of an HMAC: creating a signature, and verifying a signature.
"""
class Notary(object):
	def __init__(self):
		pass

	"""
	Hashes some data and signs it with a prv key.

	@data: Some raw string of bytes to hash and sign.
	@prvKeyPath: The path to some RSA-private key file; the Crypto libs use file names as their primary
	access point to keys.

	Returns a signature encoded as a string. See https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.Signature.PKCS1_v1_5.PKCS115_SigScheme-class.html#sign
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
		#print("signature of len "+str(len(signature))+" "+str(signature))

		return  signature

	def Sign3(self, data, prvKeyPath):
		"""
		Rolled our own RSA hmac signer. No, this absolutely not secure, since we're not using padding.
		For real applications, use the Sign() function not Sign2().
		https://stuvel.eu/python-rsa-doc/usage.html#encryption-and-decryption
		"""
		if len(data) == 0:
			print("ERROR data empty, nothing to sign")
			return None

		keyData = open(prvKeyPath).read()
		pubkey = rsa.PrivateKey.load_pkcs1(keydata)
		


		h = SHA256.new()
		h.update(data)
		signature = key.encrypt(h,"abc")

		#signer = PKCS1_v1_5.new(key)
		#signature = signer.sign(h)
		print("signature of len "+str(len(signature))+" "+str(signature))

		return  signature



	def Sign2(self, data, prvKeyPath):
		"""
		Rolled our own RSA hmac signer. No, this absolutely not secure, since we're not using padding.
		For real applications, use the Sign() function not Sign2().
		https://stuvel.eu/python-rsa-doc/usage.html#encryption-and-decryption
		"""
		if len(data) == 0:
			print("ERROR data empty, nothing to sign")
			return None

		key = RSA.importKey(open(prvKeyPath).read())
		h = SHA256.new()
		h.update(data)
		signature = key.encrypt(h,"abc")

		#signer = PKCS1_v1_5.new(key)
		#signature = signer.sign(h)
		print("signature of len "+str(len(signature))+" "+str(signature))

		return  signature

	def Verify2(self, data, signature, pubKeyPath):
		key = RSA.importKey(open(pubKeyPath).read())
		h = SHA256.new(data)
		verifier = PKCS1_v1_5.new(key)
		if verifier.verify(h, signature):
			print("The signature is authentic.")
			return True	
		else:
			print("The signature is not authentic.")
			return False



	"""
	Given some data, a signature, and a path to an RSA public key file, verifies the signature.
	This just implements the verification side of an HMAC.

	Returns: False if signature is invalid, True if valid.
	"""
	def Verify(self, data, signature, pubKeyPath):
		auth = False
		key = RSA.importKey(open(pubKeyPath).read())
		h = SHA256.new(data)
		verifier = PKCS1_v1_5.new(key)
		if verifier.verify(h, signature):
			#print("The signature is authentic.")
			auth = True

		return auth

	def MakeRSAKeys(self,pubKeyPath,prvKeyPath):
		"""
		Just a convenient utility that seemed like it belongs in this class. Caller can request
		this object generate an RSA pub/prv key pair and write them to pubKeyPath and prvKeyPath as pem files.
		This is just for demo purposes; no thought has been given to security with this method.
		"""
		keys = RSA.generate(2048)
		f = open(prvKeyPath,'w+')
		f.write(keys.exportKey())
		f.close()
		f = open(pubKeyPath,"w+")
		f.write(keys.publickey().exportKey())
		f.close()





