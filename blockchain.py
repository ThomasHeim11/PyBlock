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


	
	
			