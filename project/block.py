import hashlib

class Block:

    def __init__(self, previous_hash, transaction):
        self.previous_hash = previous_hash
        self.transactions = transaction
        string_to_hash = ''.join(transaction) + previous_hash
        # hashing digital information and getting string representation
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
