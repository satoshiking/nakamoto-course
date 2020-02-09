"""
Part 1
Given a string of a sentence as input, generate a Merkle tree whose blocks are each word in the sentence (not including spaces, but including punctuation).
You will use SHA-2 as your hash function for this Merkle tree. Your function should take in a sentence as a string and return the Merkle root as a hex string.
(Remember that the raw data should be hashed first before being combined into the Merkle tree!)

Since you'll be building a binary Merkle tree, you will need to add padding if the blocks are not a power of 2.
For Merkle tree padding you will be using the 0 byte. (Literally '\x00' or chr(0) in Python.)
Note: do not use the HASH of the 0 byte, as though the 0 byte were a block of data—this would make the hash of padded data indistinguishable from the hash
of the same data with a bunch of 0s appended to it. You should literally skip the "hash the base layer" procedure for these padding nodes.

For example, given the sentence "I love chicken!" your code should Merkleize the blocks "I", "love", "chicken!", and "\x00".
The Merkle root your code returns should be "ac5544f3322e06322c6740a7c428c5cf9f2f33b88a023a3aad6d7199c31cbe29".
(Do not use any special padding for leaf nodes vs internal nodes. Nodes should be combined and hashed using simple string concatenation.)

Part 2
For part 2, you'll be verifying Merkle proofs. To verify a Merkle proof, you don't actually need the entire Merkle path—you only need the root,
the block of data for which you're proving inclusion, and all of the siblings on the way up the Merkle proof.
You also need to know which side each sibling is on (otherwise you won't know which to concatenate on which side).

Here's a visualization from the course of what that looks like:
Your function will receive the Merkle root, the data for which we're proving inclusion, and then a list of tuples of sibling hashes:
[(sibling_hash, Side.LEFT or Side.RIGHT), (sibling_hash, Side.LEFT or Side.RIGHT), ...]
Knowing which sides they're on is necessary for the correct concatenation order as you're reconstructing the Merkle path.
It may help to sketch out a few sample proofs and think through how you'd verify them.
"""

from hashlib import sha256


def merkleize(sentence: str) -> str:
    hashes = [h(x) for x in sentence.split()]

    i = 1
    while True:
        print(i, len(hashes),  'hashes =', hashes)
        if len(hashes) < 1:
            return
        elif len(hashes) == 1:
            return hashes[0]
        else:
            hashes = list(hash_of_pair(hashes))
        i += 1

def hash_of_pair(hashes):
    if len(hashes) % 2 != 0:
        hashes.append("\x00")
    for i in range(len(hashes)):
        if i % 2 == 0:
            digest1 = hashes[i]
            digest2 = hashes[i + 1]
            yield h(digest1 + digest2)

def h(s): return sha256(s.encode()).hexdigest()


from enum import Enum
class Side(Enum):
    LEFT = 0
    RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
    result = h(data)
    for (hash, Side) in proof:
        if Side.LEFT:
            result = h(hash + result)
        else:
            result = h(result + hash)
    return True if result == root else False


print('root=', merkleize('In our village, folks say God crumbles up the old moon into stars.'))
# self.assertEqual(merkleize("In our village, folks say God crumbles up the old moon into stars."), "dddf9c7317f31d40714814749dac3a0c5ebab164262d49b576ed35f95850797a")
