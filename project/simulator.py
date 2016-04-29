import signature
import update
import os
import stat
import host
import time

class Simulator(object):
	def __init__(self,newExePath,initialExePath,evilExePath,folderList,contract):
		self.newExePath = newExePath
		self.initialExePath = initialExePath
		self.evilExePath = evilExePath
		self.hostFolders = folderList
		self._pubKeyPath = "./pubKey.pem"
		self._prvKeyPath = "./prvKey.pem"
		#build the executable that the hosts will have initially
		self.initialUpdate = update.Update()
		self.initialUpdate.SetData(self.initialExePath)
		#build the update to be sent to the hosts
		self.goodUpdate = update.Update()
		self.goodUpdate.SetData(self.newExePath)
		self.evilUpdate = update.Update()
		self.evilUpdate.SetData(self.evilExePath)
		self._notary = signature.Notary()
		#evil update contains bad executable, but steals someone else's signature
		self.evilUpdate.Signature = self.goodUpdate.Signature
		self.hosts = [] #Hosts will be set-up in init()
		self.contract = contract

	def Init(self):
		"""
		Given the host folder paths, makes sure each folder contains:
			-private RSA key "prvKey.pem"
			-public RSA key "pubKey.pem"
			-the secured exe "hello.exe"
		"""
		success = False
		print("Initializing host folders, keys, and initial executable...")
		if self._initializeHostFolders():
			#make the simulator's own RSA keys
			self._notary.MakeRSAKeys(self._pubKeyPath,self._prvKeyPath)
			#Now sign the update with simulator (master) prv key
			self.goodUpdate.SignData(self._prvKeyPath)
			success = True
		else:
			print("ERROR failed to initialized host folders and keys")

		return success

	def _initializeHostFolders(self):
		"""
		Initializes all of the hosts with a pub/prv RSA key and initial executable.
		"""
		i = 1
		success = False
		for folder in self.hostFolders:
			if os.path.isdir(folder):
				#create this hosts initial local exe (just overwrite if it already exists,for testing)
				hostExePath = folder+"/myExe.exe"
				f = open(hostExePath,"w+")
				f.write(self.initialUpdate.Data)
				f.close()
				#make the file executable
				st = os.stat(hostExePath)
				os.chmod(hostExePath, st.st_mode | stat.S_IEXEC)
				#create the host's public and private keys
				pubKeyPath = folder+"/pubKey.pem"
				prvKeyPath = folder+"/prvKey.pem"
				self._notary.MakeRSAKeys(pubKeyPath,prvKeyPath)
				#build this host
				h = host.Host("127.0.0.1",5555+i,i,i,self.contract,prvKeyPath,pubKeyPath,self._pubKeyPath)
				self.hosts.append(h)
				success = True
			else:
				print("ERROR not a host folder: "+folder)
			i+=1

		return success

	def RunHostExes(self):
		"""
		Tell each host to run their current exe. This is just to demonstrate
		which file each host has, where the exe is just some message like "good hello world"/"evil hello world"
		"""
		print("Simulating current host exe's...")
		for h in self.hosts:
			h.RunExe()

	def GoodUpdateAllHosts(self):
		"""
		'Sends' the good (verifiable) signed exe to all hosts. The host will then verify and then register
		the exe on the blockchain. This simulates sending an update (or any file) to a host, though uses no
		networking api's. Each update is simply sent/received serially. Preferably the host would be separate
		processes communicating over localhost, which we could do in the future.
		"""
		for h in self.hosts:
			h.Receive(self.goodUpdate.Serialize())

	def EvilUpdateAllHosts(self,hostIndex):
		"""
		'Sends' the evil (unverifiable) signed exe to all hosts.
		"""
		i = 1
		for h in self.hosts:
			if i != hostIndex:
				h.Receive(self.goodUpdate.Serialize())
			else:
				h.Receive(self.evilUpdate.Serialize())
			i+=1

	def RegisterAll(self):
		"""
		Have every host register its received update on the contract block. This statefully assumes
		the hosts have received their updates, for simplicity.
		"""
		for h in self.hosts:
			h.Register()


	def RepollAll(self):
		"""
		Force each host to examine the consensus contract for validity.
		"""
		for h in self.hosts:
			h.PollContract()			



"""
#init the blockchain, with the consensus contract
print("building tester and contract...")
s = tester.state()
c = s.abi_contract("consensusContract.se")
#(1)init the k hosts: keys, addrs
peers = [Host(), Host(), Host(), Host()]
master = Host()
"""
