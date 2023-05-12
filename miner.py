from random import randint, random
from xxhash import xxh32
from time import time

# Settings
global zeros, MAX_NONCE
zeros = 6 #DON'T CHANGE!
MAX_NONCE = 10**10

# Generate fast hash
def sha(text):
    text = str(text)
    return xxh32(text).hexdigest()

# Check if hashes match
def check(new_hash, zeros):
    if new_hash.startswith('0'*zeros):
        return True
    else:
        return False

def mine(block):
    start_time = time()
    # New hash
    text = block["ph"] + str(block["nonce"]) + block["ts"]
    block["ph"] = sha(text)
    while True:
        text = block["ph"] + str(block["nonce"]) + block["ts"]
        
        if check(sha(text), zeros):
            print("NONCE: ", block["nonce"])
            print("Hash: ", sha(text))
            break
        block["nonce"] = randint(1, MAX_NONCE)

    print("--- %s seconds ---" % (time() - start_time))
    return block

pblock = {
  "ph": "5bb98b81",
  "nonce": 1,
  "ts": "Some transaction data"
}

# Block
ph = sha(pblock)
block = {
  "ph": ph,
  "nonce": 1,
  "ts": "Some transaction data"
}



import data
#'''
while True:
    block = mine(block)

    # Write blocks
    blocks = data.mine.read()
    blocks.append(block)
    data.mine.write(blocks)
#'''


#blocks = data.mine.read()
#print(len(blocks))
