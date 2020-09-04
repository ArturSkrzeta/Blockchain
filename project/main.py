from blockchain import BlockChain
from block import Block

def main():

    num_of_blocks = 8
    chain = BlockChain()

    genesis_block = Block('First block',['transactionXYZ'])
    chain.append(genesis_block)

    for i in range(1, num_of_blocks):
        block = Block(chain.get_block(i-1).block_hash, ['transaction' + str(i)])
        chain.append(block)

    chain.print_chain()

if __name__ == "__main__":
    main()
