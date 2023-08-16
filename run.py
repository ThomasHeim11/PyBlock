from blockchain import Blockchain
import ecdsa
import base64


def generate_ECDSA_keys():

    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex() #convert your public key to hex
    public_key = base64.b64encode(bytes.fromhex(public_key)) #we are going to encode the public key to make it shorter

    return public_key, private_key


sender, sender_private_key = generate_ECDSA_keys()
sender2, sender2_private_key = generate_ECDSA_keys()
receiver, receiver_private_key = generate_ECDSA_keys()
miner, miner_private_key = generate_ECDSA_keys()


blockchain = Blockchain()
blockchain.addTransaction(sender, receiver, 20, sender_private_key)

blockchain.addTransaction(sender2, receiver, 30, sender2_private_key)

blockchain.minePendingTransactions(miner)
print("New Block has been added to BlockChain \n")

print("🔗 Displaying the BlockChain🔗 \n")
print(blockchain.displayChain())

print("Receiver Balance 💰 ->",blockchain.getBalance(receiver))










