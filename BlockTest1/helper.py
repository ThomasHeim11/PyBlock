from ecdsa import SigningKey
import ecdsa
from hashlib import sha256


private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
msg = 10
msg = str(msg).encode()
signature = private_key.sign(msg)
public_key = private_key.get_verifying_key()
print("signature", signature)
print("Verified:", public_key.verify(signature, msg), "\n")


msg = 10
msg = str(msg).encode()
#print("Private Key as Object",private_key)
sk = private_key.to_string().hex()
#print("Private Key as hex",sk)
sk = ecdsa.SigningKey.from_string(bytes.fromhex(sk), curve=ecdsa.SECP256k1) 
#print("Private Key as Object",sk)
sing = sk.sign(msg)
print("sing", sing)
print("\n")

msg = 10
msg = str(msg).encode()
#print("Public Key as Object",public_key)
vk = public_key.to_string().hex()
#print("Public Key as hex",vk)
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk), curve=ecdsa.SECP256k1) 
print(vk)
print("Public Key as Object",vk)
print("Verified:", vk.verify(sing, msg), "\n")