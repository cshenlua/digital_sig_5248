from Crypto.PublicKey import RSA
from hashlib import sha256

# Key Pair generation (Public and Private)
keyPair = RSA.generate(bits=1024)
print(f"Public key: (n={int(keyPair.n)}, e={int(keyPair.e)})")
print(f"Private key: (n={int(keyPair.n)}, e={int(keyPair.d)})")

# Signing the message 

msg = b'Hello, Bob!'
hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
sig = pow(hash,keyPair.d, keyPair.n)
# print("Signature:", int(sig))

# Verify signature 
hashFromSignature = pow(sig,keyPair.e,keyPair.n)
print("Hash:", hash)
print("Hash from Signature:", hashFromSignature)
print("Signature valid:", hash == hashFromSignature)