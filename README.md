# PyBlock

## :snake: Building a Blockchain from scratch in Python.
### :link: I built this Blockchain in Python to better understand how a Blockchain works

![block1](https://user-images.githubusercontent.com/30176438/132985082-3256a981-01d6-4149-a154-a131ca27bde1.png)
![block2](https://user-images.githubusercontent.com/30176438/132985076-b6956ee6-4834-4a16-bc6e-d926af51bfa6.png)
![block3](https://user-images.githubusercontent.com/30176438/132985081-43ab9138-c8b1-49ab-a82b-29c70d2e9c19.png)





## :rocket: Key Takeaways

In this project, I delved into the fundamental concepts of blockchain technology and gained insights into the intricate processes that underpin its functionality. Specifically, I focused on the following key learning points:

1. **Transaction Validation and Verification:** I comprehended the crucial steps involved in validating and verifying transactions before their inclusion in a block. This understanding extends to the significance of ensuring the accuracy and authenticity of each transaction✅

2. **Block Validation and Verification:** I gained proficiency in the validation and verification procedures that a block undergoes prior to its integration into the blockchain. This involves grasping the mechanisms that guarantee the integrity and consistency of the blockchain🎊

3. **Mining and Proof of Work:** My exploration included an in-depth analysis of mining operations and the concept of proof of work. I now grasp the role of miners in securing the network and the intricate computational processes behind it⛏️

4. **Hashing Calculations:** I acquired the ability to calculate and comprehend the hashing functions applied to both transactions and blocks. This skill is essential for ensuring data integrity and maintaining the security of the blockchain🧮

5. **Transaction Signing and Verification:** I developed a clear understanding of how transactions are signed and subsequently verified, ensuring that only valid transactions are processed and added to the blockchain🪄

6. **Miner Incentives:** I now understand the rewarding system for miners and the incentives that drive them to contribute their computational power to maintain the blockchain network🤑


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

