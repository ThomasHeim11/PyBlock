from blake3 import blake3
import ecdsa
import json
import hashlib
from datetime import datetime

# msg = bytes("hello world", "utf-8")
# print("The hash of 'hello world' is", blake3(msg).hexdigest())
# print("print keys here")

# def generate_keys():
#     private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
#     public_key = private_key.get_verifying_key()

#     return public_key.to_string().hex(), private_key.to_string().hex()

# public_key, private_key = generate_keys()

# print("public key", public_key)
# print("\n")
# print("private key", private_key)


# def calculateHash(sender, receiver, amt, time):

# 		hashString = sender + receiver + str(amt) + str(time)
# 		hashEncoded = json.dumps(hashString, sort_keys=True).encode()
# 		return blake3(hashEncoded).hexdigest()
		


# time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S") 
# sender = "me"
# receiver = "you"
# amt = 10

# print(calculateHash(sender, receiver, amt, time))




from hashlib import sha256
message = b"message"
public_key = '98cedbb266d9fc38e41a169362708e0509e06b3040a5dfff6e08196f8d9e49cebfb4f4cb12aa7ac34b19f3b29a17f4e5464873f151fd699c2524e0b7843eb383'
sig = '740894121e1c7f33b174153a7349f6899d0a1d2730e9cc59f674921d8aef73532f63edb9c5dba4877074a937448a37c5c485e0d53419297967e95e9b1bef630d'

vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1, hashfunc=sha256) # the default is sha1
print(vk)
print("\n")
print(vk.verify(bytes.fromhex(sig), message) )
