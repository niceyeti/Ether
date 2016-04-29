import serpent
from ethereum import tester, utils, abi

serpent_code = '''
#alloc the host key->hash table for 10 hosts
data registrations[10][2]
consensusThreshold = 6

#set up the registration table and host keys
def init():
	self.registrations[0][0] = 0
	self.registrations[1][0] = 1
	self.registrations[2][0] = 2
	self.registrations[3][0] = 3
	self.registrations[4][0] = 4
	self.registrations[5][0] = 5
	self.registrations[6][0] = 6
	self.registrations[7][0] = 7
	self.registrations[8][0] = 8
	self.registrations[9][0] = 9

def getHostKey(i):
	return self.registrations[i][0]

#look up a registered hash for some host
def readHash(index):
	hash = -1
	if index < 10 and index > -1:
		hash = self.registrations[index][1]
	return hash


#A host submits their hash
def submitHash(index,hash):
	success = False

	if index < 10 and index > -1:
		self.registrations[index][1] = hash
		success = True

	return success

def consensus(a):
	d = array(5)
	d[0] = 3
	d[1] = 2
	d[2] = 2
	d[3] = 4
	d[4] = 5


	log(a)
	log(tx.origin)
	i = 0
	while i < 10:
		log(i)
		i+=1

	return(sha256(d,items=5))

'''

#sets up genesis block of the tester
s = tester.state()
c = s.abi_contract(serpent_code)
#o = c.main(5)
#print(str(o))
o = c.consensus(3)
print(str(o))
print("tester.k8: "+str(tester.k8))

print("getHostKey(1) result: "+str(c.getHostKey(1)))


print("submitting: "+str(c.submitHash(1,12357654)))
print("reading hash: "+str(c.readHash(1)))




"""
serpent_code = '''
def foo(a):
	#I'm a comment! -Ralph Wiggum

	d = array(5)
	d[0] = 3
	d[1] = 2
	d[2] = 2
	d[3] = 4
	d[4] = 5


	log(a)
	log(tx.origin)
	i = 0
	while i < 10:
		log(i)
		i+=1

	return(sha256(d,items=5))
'''
"""
