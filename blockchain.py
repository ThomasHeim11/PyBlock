import json
import ecdsa
from datetime import datetime
from blake3 import blake3
import base64

class Blockchain():
    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = [self.addGenesisBlock()]
        self.pendingTransactions = []
        self.difficulty = 2
        self.minerRewards = 50
        self.blockSize = 10

    def displayChain(self):
        """
        Displays information about each block in the blockchain.
        """
        for block in self.chain:
            print("----------------------------------")
            print("Block Index: ", block.index)
            print("Block Transactions: ", block.transactions)
            print("Block Hash: ", block.hash)
            print("Block PrevHash: ", block.prev)
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
        """
        Mines pending transactions and adds a new block to the blockchain.
        """
        lenPT = len(self.pendingTransactions)
        if lenPT <= 1:
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
        """
        Adds a new transaction to the pending transactions list.
        """
        if not sender or not receiver or not amt:
            print("Transaction error 1")
            return False

        transaction = Transaction(sender, receiver, amt)

        if not transaction.sign_tx(senderKey):
            return False

        if not transaction.isValidTransaction():
            print("Transaction error 2")
            return False
        self.pendingTransactions.append(transaction)
        return len(self.chain) + 1

    def getLastBlock(self):
        """
        Returns the last block in the blockchain.
        """
        return self.chain[-1]

    def addGenesisBlock(self):
        """
        Adds the initial genesis block to the blockchain.
        """
        tArr = []
        tArr.append(Transaction("Satoshi", "Me", 10))
        genesis = Block(tArr, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 0)

        genesis.prev = "None"
        return genesis

    def isValidChain(self):
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            b1 = self.chain[i-1]
            b2 = self.chain[i]

            if not b2.hasValidTransactions():
                print("Error 3: Invalid transactions")
                return False

            if b2.hash != b2.calculateHash():
                print("Error 4: Invalid hash")
                return False

            if b2.prev != b1.hash:
                print("Error 5: Invalid previous hash")
                return False
        return True

    def getBalance(self, person):
        """
        Returns the balance of a person in the blockchain.
        """
        balance = 0
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            try:
                for j in range(0, len(block.transactions)):
                    transaction = block.transactions[j]
                    if transaction.sender == person:
                        balance -= transaction.amt
                    if transaction.receiver == person:
                        balance += transaction.amt
            except AttributeError:
                print("No transactions")
        return balance

class Block():
    def __init__(self, transactions, time, index):
        """
        Initializes a block with transactions, time, and index.
        """
        self.index = index
        self.transactions = transactions
        self.time = time
        self.prev = ''
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        """
        Calculates the hash of the block.
        """
        hashTransactions = ""

        for transaction in self.transactions:
            hashTransactions += transaction.id
        hashString = str(self.time) + hashTransactions + self.prev + str(self.nonce)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return blake3(hashEncoded).hexdigest()

    def mineBlock(self, difficulty):
        """
        Mines the block with the given difficulty level.
        """
        arr = []
        for i in range(0, difficulty):
            arr.append(i)
        
        # Compute until the beginning of the hash = 0123..difficulty
        arrStr = map(str, arr)
        hashPuzzle = ''.join(arrStr)
        
        while self.hash[0:difficulty] != hashPuzzle:
            self.nonce += 1
            self.hash = self.calculateHash()
            if (self.nonce % 100) == 0:
                print("⌛ Please Hold On, ⛏️⛏️ MINING BLOCK ⛏️⛏️ \n")
            
        print("Block Mined!")
        return True

    def hasValidTransactions(self):
        """
        Checks if all transactions in the block are valid.
        """
        for i in range(0, len(self.transactions)):
            transaction = self.transactions[i]
            if not transaction.isValidTransaction():
                return False
        return True

class Transaction():
    def __init__(self, sender, receiver, amt):
        """
        Initializes a transaction with sender, receiver, and amount.
        """
        self.sender = sender
        self.receiver = receiver
        self.amt = amt
        self.time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.id = self.calculateHash()
        self.signature = ""

    def calculateHash(self):
        """
        Calculates the hash of the transaction.
        """
        hashString = str(self.sender) + str(self.receiver) + str(self.amt) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return blake3(hashEncoded).hexdigest()

    def isValidTransaction(self):
        """
        Validates the transaction's integrity and signature.
        """
        if self.id != self.calculateHash():
            print("Hash Problem")
            return False
        
        if self.sender == self.receiver:
            print("Sender = Receiver, Please Change Receiver Address")
            return False
        
        if self.sender == "Miner Rewards":
            # Needs more work
            return True

        # Using Public Key to verify
        message = str(self.amt)
        public_key = (base64.b64decode(self.sender)).hex()
        signature = base64.b64decode(self.signature)
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
        verify = vk.verify(signature, message.encode())
        
        if verify:
            print("Transaction Verified!")
            return True
        else:
            print("Signature Verification Error")
            return False

    def sign_tx(self, private_key):
        """
        Signs the transaction using the provided private key.
        """
        message = str(self.amt)
        bmessage = message.encode()
        sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        signature = base64.b64encode(sk.sign(bmessage))
        self.signature = signature
        return True
