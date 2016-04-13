import serpent
from ethereum import tester, utils, abi

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

#sets up genesis block of the tester
s = tester.state()
c = s.abi_contract(serpent_code)
#o = c.main(5)
#print(str(o))
o = c.foo(3)
print(str(o))

