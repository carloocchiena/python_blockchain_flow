import hashlib
import json
from time import time 

# this is the blockchain base structure
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        
        self.new_block(previous_hash = "Aziona founded 15/02/2021", proof = 100)
        
    def new_block(self, proof, previous_hash=None):
        block = {                                                       # JSON element that define the block 
        "index": len(self.chain) + 1,                                   # take length of our blockchain and add 1 (index of current new_block)
        "timestamp": time(),                                            # timestamp
        "transaction": self.pending_transactions,                       # all pending transactions will be included in the new block
        "proof": proof,                                                 # confirming a valid nonce 
        "previous_hash": previous_hash or self.hash(self.chain[-1]),    # hashed version of the most recent approved block 
        }
    
        self.pending_transactions = []
        self.chain.append(block)
    
        return block
    
    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {                                                 # defining JSON obj for the new transaction; this time is a container 
        "sender":sender,
        "recipient": recipient,
        "amount": amount
        }
    
        self.pending_transactions.append(transaction)                   # append the trasaction to the pending list
        return self.last_block["index"] + 1
    
    #write the hashing function

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
    
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
    
        return hex_hash
    
blockchain = Blockchain()
t1 = blockchain.new_transaction("Alice", "Bob", "1 BTC")
t2 = blockchain.new_transaction("Vitalik", "Satoshi", "3 BTC")
t3 = blockchain.new_transaction("Satoshi", "Vitalik", "5 BTC")
blockchain.new_block("Hello_World")

t4 = blockchain.new_transaction("Alice", "Bob", "6 BTC")
t5 = blockchain.new_transaction("Alice", "Satoshi", "7 BTC")
t6 = blockchain.new_transaction("Bob", "Vitalik", "5 BTC")
blockchain.new_block("HODL")

t7 = blockchain.new_transaction("Mario", "Luigi", "6 BTC")
t8 = blockchain.new_transaction("Bart", "Homer", "7 BTC")
t9 = blockchain.new_transaction("Ryu", "Ken", "5 BTC")
blockchain.new_block("Memes")

print ("Blockchain: ", blockchain.chain)
