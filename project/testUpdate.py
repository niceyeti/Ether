from __future__ import print_function
import hashlib
import update
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random

"""
NOTE This code should never be used for anything real. Its just a demo. Reading prv keys
into the script environment shouldn't be done.
"""
#Generate pub and prv key, and store them in files
prvKeyPath = "prvKey.pem"
pubKeyPath = "pubKey.pem"
key = RSA.generate(1024)
f = open(prvKeyPath,'w+')
f.write(key.exportKey('PEM'))
f.close()
f = open(pubKeyPath,'w+')
f.write(key.publickey().exportKey('PEM'))
f.close()

#Create Update object, with signature
u = update.Update("hello.exe",prvKeyPath)

print(u.Verify(pubKeyPath))





#>>> f = open('mykey.pem','r')
#>>> key = RSA.importKey(f.read())










"""
kPub, kPrv = rsa.newkeys(1024)
print("Keys: "+str(kPrv)+"\n"+str(kPub))
u = update.Update("hello.exe",kPrv)
print(str(u.Data))
print(str(u.Signature))
ser = u.Serialize()
data = u.Data
print("Serialized: "+ser)
u.Deserialize(ser)
print("s == deserialized: "+str(data == u.Data))
print("Verified signature: "+u.Authenticate(kPub))
"""








