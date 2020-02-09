import merkletools

sentence = 'I love chicken!'
# sentence = 'In our village, folks say God crumbles up the old moon into stars.'
input_words = [x for x in sentence.split()]
print(input_words)


mt = merkletools.MerkleTools()
mt.add_leaf(input_words,True)
print('leaves = ', mt.leaves)
print('hashes_of_leaves_in_hex = ', [x.hex() for x in mt.leaves])


mt.make_tree()
print("root = %s" % mt.get_merkle_root())
