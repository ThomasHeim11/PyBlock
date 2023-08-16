import base64
import json
from datetime import datetime

import ecdsa
from blake3 import blake3


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
	
def addTransaction(self, sender, recevierm, amt, senderKey):
	#DECODE SENDER RECEIVER KEY IN test FILE

	if not sender or not receiver or not amt:
		print("transacation error 1")
		return False
	
	transaction = Transaction(sender, reciver, amt)

	if not transaction.sign_tx(senderKey):
		return False
	
	if not transaction.isValidTransaction():
		print("transaction error 2")
		return False
	self.pendingTransaction.append(transaction)
	return len(self.chain) + 1

def getLastBlock(self):
	tArr = []
	tArr.append(Transaction("Satoshi", "Me", 10))
	genesis = Block(tArr, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 0)

	genesis.prev = "None"
	return genesis

def isValidChain(self):
	for i in range(1, len(self.chain)):
		bi = self.chain[i-1]
		b2 = self.chain[i]

		if not b2.hashValidTransaction():
			print("error 3")
			return False
		
		if b2.hash != b2.calculateHash():
			print("error 4")
			return False
		
		if b2.prev != b1.hash:
			print("error 5")
			return False
		
	return True

def getBalanc(self, person):
	balance = 0
	for i in range(1, len(self.chain)):
		block = self.chain[i]
		try:
				for j in range(0, len(block.transactions)):
					transaction = block.transactions[j]
					if(transaction.sender == person):
						balance -= transaction.amt
					if(transaction.reciver == person):
						balance += transaction.amt
		except AttributeError:
			print("no transaction")
	return balance 






	
	
			