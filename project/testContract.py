import serpent
from ethereum import tester, utils, abi

#sets up genesis block of the tester
print("building tester and contract...")
s = tester.state()
c = s.abi_contract("consensusContract.se")
#o = c.main(5)
#print(str(o))
#o = c.consensus(3)
#print(str(o))

#Remember the test has a bunch of keys itself, which may be useful
#print("tester.k8: "+str(tester.k8))
#print("getHostKey(1) result: "+str(c.getHostKey(1)))
#print("submitting: "+str(c.registerHash(1,12357654)))
#print("reading hash: "+str(c.readHash(1)))

#A very simple test: passed if hash can be written and then read out again
"""
hsh1 = ""
for i in range(0,256):
	hsh1 += "a"
print("len: "+str(len(hsh1)))
hsh1 = 13456789
hst = 1
c.registerHash(hst,hsh1)
hsh2 = c.readHash(hst)
if hsh2 == hsh1:
	print("Test PASSED: hash "+str(hsh1)+" written and read successfully to/from host "+str(hst))
else:
	print("Test FAILED. Wrote hash "+str(hsh1)+" to host "+str(hst)+" but read hash "+str(hsh2))

#print(str(c.getMyString()))

print(str(c.passArray(['A','B'])))
"""

"""
l = [93, 85, 223, 247, 190, 49, 83, 250, 76, 231, 247, 103, 237, 245, 119, 114, 203, 215, 44, 251, 137, 145, 142, 87, 77, 247, 69, 229, 0, 182, 92, 126, 4, 145, 150, 219, 167, 49, 165, 28, 5, 183, 141, 222, 189, 137, 206, 12, 228, 99, 168, 200, 225, 194, 98, 171, 86, 137, 110, 152, 250, 198, 198, 161, 67, 108, 176, 251, 141, 10, 121, 164, 28, 150, 207, 36, 178, 95, 223, 39, 64, 21, 29, 82, 178, 37, 43, 171, 167, 157, 190, 207, 128, 107, 32, 96, 22, 74, 19, 195, 255, 177, 229, 155, 226, 107, 114, 82, 164, 237, 89, 45, 41, 108, 83, 53, 165, 84, 172, 116, 183, 151, 45, 148, 244, 56, 26, 189, 97, 240, 156, 227, 136, 142, 20, 121, 70, 9, 105, 91, 117, 4, 70, 201, 250, 170, 114, 159, 80, 254, 215, 237, 160, 59, 150, 83, 86, 130, 179, 80, 78, 251, 219, 194, 131, 153, 162, 106, 186, 6, 12, 138, 179, 43, 255, 152, 140, 217, 226, 42, 111, 250, 14, 116, 201, 149, 50, 218, 122, 126, 68, 142, 74, 139, 239, 253, 123, 188, 30, 176, 58, 134, 217, 229, 45, 247, 226, 102, 49, 72, 190, 183, 8, 4, 39, 198, 148, 181, 220, 168, 150, 192, 53, 30, 165, 170, 128, 230, 203, 57, 255, 123, 136, 36, 130, 84, 84, 192, 217, 236, 183, 83, 157, 92, 54, 16, 193, 55, 17, 218, 240, 117, 204, 53, 23, 161]
l = [93, 85, 223, 247, 190, 49, 83, 250, 76, 231, 247, 103, 237, 245, 119, 114, 203, 215, 44, 251, 137, 145]#, 142, 87, 77, 247, 69, 229, 0, 182, 92, 126, 4, 145, 150, 219, 167, 49, 165, 28, 5, 183, 141, 222, 189, 137, 206, 12, 228, 99, 168, 200, 225, 194, 98, 171, 86, 137, 110, 152, 250, 198, 198, 161, 67, 108, 176, 251, 141, 10, 121, 164, 28, 150, 207, 36, 178, 95, 223, 39, 64, 21, 29, 82, 178, 37, 43, 171, 167, 157, 190, 207, 128, 107, 32, 96, 22, 74, 19, 195, 255, 177, 229, 155, 226, 107, 114, 82, 164, 237, 89, 45, 41, 108, 83, 53, 165, 84, 172, 116, 183, 151, 45, 148, 244, 56, 26, 189, 97, 240, 156, 227, 136, 142, 20, 121, 70, 9, 105, 91, 117, 4, 70, 201, 250, 170, 114, 159, 80, 254, 215, 237, 160, 59, 150, 83, 86, 130, 179, 80, 78, 251, 219, 194, 131, 153, 162, 106, 186, 6, 12, 138, 179, 43, 255, 152, 140, 217, 226, 42, 111, 250, 14, 116, 201, 149, 50, 218, 122, 126, 68, 142, 74, 139, 239, 253, 123, 188, 30, 176, 58, 134, 217, 229, 45, 247, 226, 102, 49, 72, 190, 183, 8, 4, 39, 198, 148, 181, 220, 168, 150, 192, 53, 30, 165, 170, 128, 230, 203, 57, 255, 123, 136, 36, 130, 84, 84, 192, 217, 236, 183, 83, 157, 92, 54, 16, 193, 55, 17, 218, 240, 117, 204, 53, 23, 161]
print(str(c.registerHash2(1,l)))
print(str(c.readHash2(1)))
"""




l = [93, 85, 223, 247, 190, 49, 83, 250, 76, 231, 247, 103, 237, 245, 119, 114, 203, 215, 44, 251, 137, 145, 142, 87, 77, 247, 69, 229, 0, 182, 92, 126, 4, 145, 150, 219, 167, 49, 165, 28, 5, 183, 141, 222, 189, 137, 206, 12, 228, 99, 168, 200, 225, 194, 98, 171, 86, 137, 110, 152, 250, 198, 198, 161, 67, 108, 176, 251, 141, 10, 121, 164, 28, 150, 207, 36, 178, 95, 223, 39, 64, 21, 29, 82, 178, 37, 43, 171, 167, 157, 190, 207, 128, 107, 32, 96, 22, 74, 19, 195, 255, 177, 229, 155, 226, 107, 114, 82, 164, 237, 89, 45, 41, 108, 83, 53, 165, 84, 172, 116, 183, 151, 45, 148, 244, 56, 26, 189, 97, 240, 156, 227, 136, 142, 20, 121, 70, 9, 105, 91, 117, 4, 70, 201, 250, 170, 114, 159, 80, 254, 215, 237, 160, 59, 150, 83, 86, 130, 179, 80, 78, 251, 219, 194, 131, 153, 162, 106, 186, 6, 12, 138, 179, 43, 255, 152, 140, 217, 226, 42, 111, 250, 14, 116, 201, 149, 50, 218, 122, 126, 68, 142, 74, 139, 239, 253, 123, 188, 30, 176, 58, 134, 217, 229, 45, 247, 226, 102, 49, 72, 190, 183, 8, 4, 39, 198, 148, 181, 220, 168, 150, 192, 53, 30, 165, 170, 128, 230, 203, 57, 255, 123, 136, 36, 130, 84, 84, 192, 217, 236, 183, 83, 157, 92, 54, 16, 193, 55, 17, 218, 240, 117, 204, 53, 23, 161]
l1 = l[0:(len(l)/2)]
l2 = l[(len(l)/2):]
print(str(l1))
print("lens: "+str(len(l1))+" "+str(len(l2)))
print(c.copyHashBlock(1,0,l1))
print(c.copyHashBlock(1,128,l2))
print(str(c.readHash2(1)))




