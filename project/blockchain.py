class BlockChain:

    def __init__(self):
        self.blocks = []

    def append(self, block):
        self.blocks.append(block)

    def print_chain(self):
        counter = 0
        for block in self.blocks:
            print('block ' + str(counter) + ': ' + block.block_hash)
            counter += 1

    def get_block(self, index):
        return self.blocks[index]
