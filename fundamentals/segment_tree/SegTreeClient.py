import random
from tqdm import tqdm
from utils.DSUtils import get_array_print_string_as_complete_binary_tree
from SumSegmentTree import SumSegmentTree
from EffSumSegTree import EffSumSegmentTree

random.seed(0)
maxVal = 10
# items = random.sample(list(range(maxVal)), n)
i = 6
tsi = 1
for n in range(i, i+1):
    items = random.choices(list(range(1, maxVal + 1)), k=n)
    print(items)
    # segTree = SumSegmentTree(tsi=tsi)
    segTree = EffSumSegmentTree()
    segTree.build(items)
    print(get_array_print_string_as_complete_binary_tree(segTree.tree[1:]))

print(segTree.query(0, 5))
print(segTree.query(0, 6))
print(segTree.query(0, 4))
print(segTree.query(2, 2))
print(segTree.query(2, 3))

# ps = get_array_print_string_as_complete_binary_tree(segTree.tree)
# print(items)
# print(ps)