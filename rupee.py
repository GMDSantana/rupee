###########################################################
# RUPEE - A SIMPLE WEE EXAMPLE OF A SIMPLE WEE BLOCKCHAIN #
#                 code based on SavjeeCoin                #
###########################################################

# Improvements suggestions:
#	mining rewards
#	smart contracts
#	transactions
#	fix the chain in case of is_chain_valid() is False

import hashlib

class Block:
	
	# Constructor
	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.nonce = 0
		self.h = self.calculate_hash()
		return None

	# Calculates this block's hash based on this block's attributes
	def calculate_hash(self):
		aux = hashlib.sha256(bytes(self.timestamp + self.data + self.previous_hash + str(self.nonce), encoding='utf-8')).hexdigest()
		return aux

	# Makes mining difficult (Proof-of-Work: for bitcoin, it is around 10 minutes per block)
	def mine_block(self, difficulty):
		if difficulty <= 0:
			return None

		while self.h[:difficulty] != '0' * difficulty:
			self.nonce = self.nonce + 1
			self.h = self.calculate_hash()
		return None


class Blockchain:
	
	# Constructor
	def __init__(self):
		self.chain = []
		self.chain.append(self.create_genesis_block())
		self.difficulty = 3
		return None

	# The first block of a blockchain
	def create_genesis_block(self):
		return Block("04/06/2018", "Genesis Block", "0")

	# Returns the latest block of this blockchain
	def get_latest_block(self):
		return self.chain[len(self.chain)-1]

	def add_block(self, new_block):
		new_block.previous_hash = self.get_latest_block().h
		new_block.mine_block(self.difficulty)
		self.chain.append(new_block)

	def is_chain_valid(self):
		for i in range(1, len(self.chain)):
			current_block = self.chain[i]
			previous_block = self.chain[i-1]

			if current_block.h != current_block.calculate_hash():
				return False

			if current_block.previous_hash != previous_block.h:
				return False
		
		return True


rupee = Blockchain()
print("First Block: ")
print("Timestamp: " + rupee.chain[0].timestamp)
print("Data: " + rupee.chain[0].data)
print("Previous Block: " + rupee.chain[0].previous_hash)
print("Nonce: " + str(rupee.chain[0].nonce))
print("Block Hash: " + str(rupee.chain[0].h))

bl = Block("04/06/2018", '5', '')
rupee.add_block(bl)

print()
print("Second Block: ")
print("Timestamp: " + rupee.chain[1].timestamp)
print("Data: " + rupee.chain[1].data)
print("Previous Block: " + rupee.chain[1].previous_hash)
print("Nonce: " + str(rupee.chain[1].nonce))
print("Block Hash: " + rupee.chain[1].h)

bl = Block("04/06/2018", '10', '')
rupee.add_block(bl)

print()
print("Third Block: ")
print("Timestamp: " + rupee.chain[2].timestamp)
print("Data: " + rupee.chain[2].data)
print("Previous Block: " + rupee.chain[2].previous_hash)
print("Nonce: " + str(rupee.chain[2].nonce))
print("Block Hash: " + str(rupee.chain[2].h))


#rupee.chain[2].h = 'ljf8few89fjijio'
#rupee.chain[2].previous_hash = 'ljf8few89fjijio'

print()
print("Is chain valid?: " + str(rupee.is_chain_valid()))
