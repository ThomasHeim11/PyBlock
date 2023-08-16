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


		return True




	
	
			