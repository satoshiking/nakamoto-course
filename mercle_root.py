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
