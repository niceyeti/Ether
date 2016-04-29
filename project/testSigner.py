import signature


signer = signature.Notary()

data = "data"
pubk = "./pubKey.pem"
prvK = "./prvKey.pem"

signer.Sign2(data,prvK)




