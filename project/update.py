from __future__ import print_function
import signature
import base64

"""
An update object consists of some data and a signature.

This is a gross simplification of what would be sent to some host:
	-the update exe
	-the signed hash of the exe

Requirements/dependencies:
This class calls methods of the Crypto.PublicKey RSA package, indirectly through
object passed in.

See usage at http://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python
"""
class Update(object):
	Data = ""
	Signature = ""

	def __init__(self):
		"""
		@exeFile: path to some executable to be sent to host
		@kPrv: Private key of the sender, used for signing the data
		"""
		self._notary = signature.Notary()
		self.Data = ""
		self.Signature = "HANCOCK"
		self.Sep = "####" #magical anchor for split operator; just something not in base64 alphabet
	
	def Init(self,exePath,prvKeyPath):
		self.SetData(exePath)
		self.SignData(prvKeyPath)

	def SetData(self,filePath):
		"""
		Read in a file (presumably an exe), store in self.Data
		"""
		dataFile = open(filePath,"r")
		while True:
			chunk = dataFile.read(65536)
			if not chunk:
				break  # EOF
			self.Data += chunk
		dataFile.close()

	def SignData(self,prvKeyPath):
		"""
		Update (self.Data) is signed by taking its hash, and encrypting the hash with
		one's private key. Result is stored in self.Signature.

		@prvKey: a private key in key = RSA.generate(), where key has publickey and privatekey components.
		(see http://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python)
		"""
		if len(self.Data) == 0:
			print("ERROR no data for Update to sign")
			self.Signature = "EVE"
			return

		#Just call the notary to generate a signature
		self.Signature = self._notary.Sign(self.Data,prvKeyPath)		

		"""
		#hash the entire executable
		h = hashlib.sha256(self.Data).hexdigest()
		#sign the hash using the passed private key
		self.Signature = rsa.encrypt(h,kPrv)
		#and base64 the whole signature
		self.Signature = base64.standard_b64encode(self.Signature)
		"""

	def Serialize(self):
		"""
		Base64's the entire object
		"""
		return base64.standard_b64encode(self.Data+self.Sep+self.Signature)

	def Deserialize(self,data):
		"""
		Given some data, split at Sep, and populate self.Data and self.Signature
		"""
		success = False
		#decode the data from base64 and split at sep to get Data and Signature
		try:
			dec = base64.standard_b64decode(data)
			#print("Decoded:"+dec)
			decoded = dec.split(self.Sep)
			if len(decoded) != 2:
				print("ERROR received "+str(len(decoded))+" Update elements but expected only two (Data and Signature)")
			else:
				self.Data = decoded[0]
				self.Signature = decoded[1]
				success = True
		except binascii.Error:
			print("ERROR could not deserialize string since it is not base64: "+data)

		return success

	def Verify(self,pubKeyPath):
		"""
		Given Data and Signature have been received/populated, this authenticates the update using the public
		key of the sender.
		"""
		if len(self.Data) == 0 or len(self.Signature) == 0:
			print("ERROR data or signature empty, nothing to authenticate (?)")
			return False
		
		return self._notary.Verify(self.Data, self.Signature, pubKeyPath)

		"""
		#get the message digest
		digest = hashlib.sha256(self.Data).digest()
		#decrypt the signature, using public key of sender
		dec = rsa.decrypt(self.Signature,kPub)

		if digest == dec:
			print("Update authenticated...")
			return True
		else:
			print("WARNING Update could not be authenticated!")
			return False
		"""


