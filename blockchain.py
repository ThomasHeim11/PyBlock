import json
import ecdsa
from datetime import datetime
from blake3 import blake3
import base64

class Blockchain ():
	def __init__(self):
		self.chain = [self.addGenesisBlock()]
		self.pendingTransactions = []
		self.difficulty = 2
		self.minerRewards = 50
		self.blockSize = 10
		

	
	def displayChain(self):
		
		for block in self.chain:
			print("----------------------------------")
			print("Block Index: ",block.index)
			print("Block Transactions: ",block.transactions)
			print("Block Hash: ",block.hash)
			print("Block PrevHash: ",block.prev)
			print("\n")
			print("Transaction List: \n")
			for transaction in block.transactions:
				print("Sender: ", transaction.sender)
				print("Receiver: ", transaction.receiver)
				print("Transaction Id 🎟️ :", transaction.id)
				print("Transaction Amount 🪙:", transaction.amt, "\n")
			print("----------------------------------")
			print("\n")
			

	def minePendingTransactions(self, miner):
		
		lenPT = len(self.pendingTransactions)
		if(lenPT <= 1):
			print("Not enough transactions to mine! (Must be > 1)")
			return False
		else:
			for i in range(0, lenPT, self.blockSize):

				end = i + self.blockSize

				if i >= lenPT:
					end = lenPT

				transactionSlice = self.pendingTransactions[i:end]
				newBlock = Block(transactionSlice, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), len(self.chain))
				hashVal = self.getLastBlock().hash
				newBlock.prev = hashVal
				newBlock.mineBlock(self.difficulty)

				if self.isValidChain():
					self.chain.append(newBlock)
					print("Adding a new Block!")
					payMiner = Transaction("Miner Rewards", miner, self.minerRewards)
					self.pendingTransactions = [payMiner]
				else:
					return False

		return True

	def addTransaction(self, sender, receiver, amt, senderKey):
		#DECODE SENDER RECEIVER KEY IN test FILE
		
		if not sender or not receiver or not amt:
			print("transaction error 1")
			return False

		transaction = Transaction(sender, receiver, amt)

		if not transaction.sign_tx(senderKey):
			return False

		if not transaction.isValidTransaction():
			print("transaction error 2")
			return False
		self.pendingTransactions.append(transaction)
		return len(self.chain) + 1

	def getLastBlock(self):

		return self.chain[-1]

	def addGenesisBlock(self):
		tArr = []
		tArr.append(Transaction("Satoshi", "Me", 10))
		genesis = Block(tArr, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 0)

		genesis.prev = "None"
		return genesis

	def isValidChain(self):
		for i in range(1, len(self.chain)):
			b1 = self.chain[i-1]
			b2 = self.chain[i]

			if not b2.hasValidTransactions():
				print("error 3")
				return False

			if b2.hash != b2.calculateHash():
				print("error 4")
				return False


			if b2.prev != b1.hash:
				print("error 5")
				return False
		return True
		
	def getBalance(self, person):
		balance = 0 
		for i in range(1, len(self.chain)):
			block = self.chain[i]
			try:
				for j in range(0, len(block.transactions)):
					transaction = block.transactions[j]
					if(transaction.sender == person):
						balance -= transaction.amt
					if(transaction.receiver == person):
						balance += transaction.amt
			except AttributeError:
				print("no transaction")
		return balance


class Block ():
	def __init__(self, transactions, time, index):
		self.index = index
		self.transactions = transactions
		self.time = time
		self.prev = ''
		self.nonse = 0
		self.hash = self.calculateHash()


	def calculateHash(self):

		hashTransactions = ""

		for transaction in self.transactions:
			hashTransactions += transaction.id
		hashString = str(self.time) + hashTransactions + self.prev + str(self.nonse)
		hashEncoded = json.dumps(hashString, sort_keys=True).encode()
		return blake3(hashEncoded).hexdigest()

	def mineBlock(self, difficulty):
		arr = []
		for i in range(0, difficulty):
			arr.append(i)
		
		#compute until the beginning of the hash = 0123..difficulty
		arrStr = map(str, arr)  
		hashPuzzle = ''.join(arrStr)
		
		while self.hash[0:difficulty] != hashPuzzle:
			self.nonse += 1
			self.hash = self.calculateHash()
			if ((self.nonse % 100) == 0):
				print("⌛Please Hold On , ⛏️⛏️ MINING BLOCK ⛏️⛏️ \n")
			
		print("Block Mined!")
		return True

	def hasValidTransactions(self):
		for i in range(0, len(self.transactions)):
			transaction = self.transactions[i]
			if not transaction.isValidTransaction():
				return False
			return True
	
	
class Transaction ():
	def __init__(self, sender, receiver, amt):
		self.sender = sender
		self.receiver = receiver
		self.amt = amt
		self.time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S") #change to current date
		self.id = self.calculateHash()


	def calculateHash(self):
		hashString = str(self.sender) + str(self.receiver) + str(self.amt) + str(self.time)
		hashEncoded = json.dumps(hashString, sort_keys=True).encode()
		return blake3(hashEncoded).hexdigest()
		

	def isValidTransaction(self):
		#VERIFY TRANSACTION
		
		if(self.id != self.calculateHash()):
			print("Hash Problem \n")
			return False
		
		if(self.sender == self.receiver):
			print("Sender = Receiver, Please Change Receiver Address \n")
			return False
		
		if(self.sender == "Miner Rewards"):
			#Needs More Work
			return True
		

		#Using Public Key to verify 
		message = str(self.amt)
		public_key = (base64.b64decode(self.sender)).hex()
		signature = base64.b64decode(self.signature)
		vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
		verify = vk.verify(signature, message.encode())
		
		if verify:
			print("Transaction Verified! \n")
			return True
		else:
			print("Signature Verification Error")
			return False
		
	def sign_tx(self, private_key):
    
		message = str(self.amt)
		bmessage = message.encode()
		sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
		signature = base64.b64encode(sk.sign(bmessage))
		self.signature = signature 

		return True