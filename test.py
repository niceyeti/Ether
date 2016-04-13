import serpent
from ethereum import tester, utils, abi

serpent_code = '''
def multiply(a):
	return(a*2)
'''

#sets up genesis block of the tester
s = tester.state()
c = s.abi_contract(serpent_code)
o = c.multiply(5)
print(str(o))
