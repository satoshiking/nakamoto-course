from hashlib import sha256


def merkleize(sentence: str) -> str:
    hashes = [h(x) for x in sentence.split()]

    i = 1
    while True:
        print(i, 'hashes =', hashes)
        if len(hashes) < 1:
            return
        elif len(hashes) == 1:
            return hashes[0]
        else:
            hashes = list(hash_of_pair(hashes))
        i += 1


def hash_of_pair(a):
    if len(a) % 2 != 0:
        a.append("\x00")
    for i in range(len(a)):
        if i % 2 == 0:
            digest1 = a[i]
            digest2 = a[i + 1]
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


# merkleize('I love chicken!')
# print('root=', merkleize(''))
# print('root=', merkleize('In our village, folks say God crumbles up the old moon into stars.'))
print('root=', merkleize('I love chicken!'))

# print()
# print(h("6ace2c1ff2db078fb835ce34180aa6ce272053ec4ac2f4ee469012f9a4a43a34" + "\x00"))
# print('a=',a)
# b = h( h("chicken!") + "\x00" )
# print('b=',b)
# print( h(a + b) )


# self.assertEqual(merkleize("In our village, folks say God crumbles up the old moon into stars."), "dddf9c7317f31d40714814749dac3a0c5ebab164262d49b576ed35f95850797a")
print('h(in)=', h("In"), 'h(out)=', h("our"))
print(h(h("In") + h("our")))
print('h(village,)=', h("village,"), 'h(folks)=', h("folks"))
print(h(h("village,") + h("folks")))
print(h(h("say") + h("God")))
print(h(h("crumbles") + h("up")))
print(h(h("the") + h("old")))
print(h(h("moon") + h("into")))
print(h(h("stars.") + "\x00"))

