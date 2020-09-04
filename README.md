<h2>Blockchain</h2>

<h3>Intro</h3>
<ul>
  <li>Data structure that ensures data integrity with its security built-in mechanizms.</li>
  <li>Built-in mechanizms prevent users from arbitrarily change the data in it.</li>
  <li>Bitcoin uses blockchain to store and verify transactions.</li>
</ul>

<h3>Python</h3>
<ul>
  <li>Below example shows how following blocks depends on the preceding ones.</li>
  <li>Every following block has its own hash and the hash of the preceding block assigned except for the first block.</li>
  <li>Small change on first block affects change of blocks hashes all the way through.</li>
  <br>
  <img src="images/blockchain.gif">
</ul>

<h3>Notes</h3>
<ul>
  <li>Chain of blocks that contain information.</li>
  <li>Each block contains data, hash and hash of previous block.
    <br>
    - data stored inside a block depends on type of blockchain <br>
    - hash, as a fingerprint, is unique and identifies a block with all of its content - it's being calculated once block created <br>
    - changing something inside the block causes the block's hash to change (that detects any atttempts of changes to block) <br>
    - hash of the previous block actually creates a chain <br>
    - having blocks chained in that way, it ensures security of the blockchain <br>
    - changing one block would make all of the following blocks in the chain invalid because of invalid 'has of previous block'
    - changing one block way back in the chain it would affect all of the hashes of blocks going forward
  </li>
  <br>
  <li>Additional security mechanism is the proof-of-work:
    <br>
    - recalculating new hashes can be performed very fast so it's not enough to keep blockchain secure <br>
    - proof-of-work mechanism slows down the creation of new blocks <br>
    - f.e. for bitcoin proof-of-work consumes 10 minutes to add new block to the chain <br>
    - because of proof-of-work, changes to one block would require recalculating the proof-of-work for all of the following block within the chain <br>
  </li>
  <br>
  <li>It's distributed which increases security level
    <br>
    - is uses peer-to-peer network <br>
    - when someone joins network he gets full copy of the blockchain - the node <br>
    - if there is an attempt to change the block it will be rejected by the rest of the nodes in the network <br>
    - the changes would be possible when affecting more than 50% of the network nodes at once which is very hard <br>
  </li>
  <br>
  <li>To make change to block you would need to change all of the blocks in the chain, recalculate the proof-of-work for each block and take control of min 50% of peer-to-peer network nodes. That sounds like impossible mission.</li>
  <br>
  <li>Blockchain with security mechanizms stays stable and steady.</li> 
</ul>
