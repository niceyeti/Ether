import socket
import signature
import update
import subprocess

class Host(object):
	def __init__(self,address,port,hostNumber,hostKey,contract,prvKeyPath,pubKeyPath,trustedPubKeyPath):
		self.addr = address
		self.port = port
		self.hostNumber = hostNumber
		self.hostKey = hostKey
		self.contract = contract
		self.exePath = "h"+str(hostNumber)+"/hello.exe"	
		self.prvKeyPath = prvKeyPath
		self.pubKeyPath = pubKeyPath
		self.trustedPubKeyPath = trustedPubKeyPath
		self.notary = signature.Notary()
		self.binData = ""
		self.update = None

	def RunExe(self):
		"""
		Clients (in this case just a test simulator) can call this to demonstrate which exe a "host" hast.
		"""
		#Run the exe
		print("Host "+str(self.hostNumber)+" running current exe: "+self.exePath)
		subprocess.call([self.exePath])
		
	def Receive(self,b64data):
		"""
		This would normally block in a read()/listen() call on a socket, but here just receives
		data serially by the caller to simplify testing.
		"""
		success = False
		#print("Received update: "+b64data)
		self.update = update.Update()
		if self.update.Deserialize(b64data):
			#verify the signature of the update
			if self.update.Verify(self.trustedPubKeyPath):
				#print("Host "+str(self.hostNumber)+" received valid update")
				success = True
			else:
				#untrusted data received, host should now go back to init state and listen for incoming data
				print("Untrusted or corrupted file received; update aborted.")
		else:
			print("ERROR update could not be deserialized by host "+str(self.hostNumber))

		return success
		
	def _hashStrToNumber(self,hashStr):
		"""
		Its not convenient to store the full 256-char hash from the crypto libs as a value
		on the blockchain, and serpent doesn't accept such large strings anyway. So instead,
		a simply sum of the chars of the hashes are kept on the blockchain as a pseudo-hash.
		If there are collisions, we could distribute the hashes with a better hash function.
		"""
		return hash(hashStr)

	"""
	Expect signature is a binary string.
	"""
	def _registerSignature(self,binSignature):
		sig = [ord(hx) for hx in list(binSignature)]
		#write the signature to block in four blocks; this is due to some unknown size constraint on data that can be passed to the contract
		blk1 = sig[0:64]
		blk2 = sig[64:128]
		blk3 = sig[128:192]
		blk4 = sig[192:256]

		result = (self.contract.copyHashBlock(self.hostKey,0,blk1) == 1)
		result = result and (self.contract.copyHashBlock(self.hostKey,64,blk2) == 1)
		result = result and (self.contract.copyHashBlock(self.hostKey,128,blk3) == 1)
		result = result and (self.contract.copyHashBlock(self.hostKey,192,blk4) == 1)

		return result

	def Register(self):
		"""
		After verifying a received update/file, sign it and register the hash on the blockchain.
		"""
		success = False
		signature = self.notary.Sign(self.update.Data,self.prvKeyPath)
		#print("host "+str(self.hostKey)+" registering signature of len "+str(len(signature))+"  "+str(list(signature)))
		if self._registerSignature(signature):
			#print("Host "+str(self.hostNumber)+ " with key "+str(self.hostKey)+" registered signature on block: "+str(signature))
			print("Host "+str(self.hostNumber)+" registered signature on block.")
			success = True
		else:
			print("ERROR host "+str(self.hostKey)+" failed to register signature on block: "+str(signature))

		return success

	def _readHash(self,hostIndex):
		"""
		Reads the hash of a hostIndex on the blockchain, which is returned as a list of 256 integers in range 0-255.
		This function wraps the call and returns the signature as a binary string.
		"""
		h = self.contract.readHash2(hostIndex)
		#print("READ HASH: "+str(h))
		return "".join([chr(n) for n in h])		

	def PollContract(self):
		"""
		The idea is for a host to monitor the consensus block, waiting for enough
		valid signatures to be received before committing the received update.
		For testing, it is assumed the block has already been fully registered, such
		that when the simulator calls this, the host can examine the consensus block in
		a single pass and either commit the update, or bail out due to some failure. A
		failure occurs if the consensus block does not contain enough valid signatures
		from other peers.

		Returns true iff all signatures are verified.
		"""
		validSigs = 0
		success = False

		#note this loop includes this host checking its own signature
		for i in range(1,6): #range(1,6) is [1,2,3,4,5] (no 6)
			h = self._readHash(i)
			#h = self.contract.readHash2(i)	
			#print("host read hash len "+str(len(h))+" from contract: "+str(h))
			if self.notary.Verify(self.update.Data,h,"./h"+str(i)+"/pubKey.pem"):
				validSigs += 1
			else:
				print("WARNING Host "+str(self.hostNumber)+" found unverified host "+str(i)+" signature")

		if validSigs == 5:
			print("Host "+str(self.hostNumber)+" verified all signatures on block.")
			#commit

			success = True
		else:
			print("Host "+str(self.hostNumber)+" verified only "+str(validSigs)+" signatures on block.")

		return success





