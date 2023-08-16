# PyChain

## :snake: Building a Blockchain from scratch in Python.
### :link: I built this Blockchain in Python to better understand how a Blockchain works

![block1](https://user-images.githubusercontent.com/30176438/132985082-3256a981-01d6-4149-a154-a131ca27bde1.png)
![block2](https://user-images.githubusercontent.com/30176438/132985076-b6956ee6-4834-4a16-bc6e-d926af51bfa6.png)
![block3](https://user-images.githubusercontent.com/30176438/132985081-43ab9138-c8b1-49ab-a82b-29c70d2e9c19.png)





## :rocket: What did I learn?

1. How a Transaction is validated & verified before adding it to a Block
2. How a Block is validated & verified before adding it to a Blockchain
3. What is mining, proof of work and how it works
4. How to calculate hashing on transaction and block
5. How transactions are signed and verified 
6. How a miner gets rewarded 


## :rocket: Features Yet to be Added
I still need to work on distributed consensus part.

## Dockerized Local Blockchain built in Python
## 🛸How to run?

### After Cloning the Repository

## Step 1: Build The Docker Image

  ```sh
  docker build -t pychain .
  ```
## Step 2: Start The Docker Container

  ```sh
  docker run --name pyblocks pychain
  ```



#### If you are unable to see emojis in the output, try running the container from the terminal of code editor (Works in VS Code)
------------------------------------------------------------------------------------------------------------------------------------

## :mag: How does it work?

### Run.py 
1. Generate Keys for sender1, sender2, receiver, and miner
2. Create the blockchain
3. Add Transaction [Sender1 sends money to Receiver]
4. Add another Transaction [Sender2 sends money to Receiver]
5. Miner validates the pending transactions, adds the transaction to a block, mines the block, and adds it to the Blockchain
6. We can see the status of the Blockchain
7. We can see the account balance of the Receiver

