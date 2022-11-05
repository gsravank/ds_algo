import random
from collections import Counter


random.seed(3)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.str = f'{val[0]},{val[1]}'
        self.left = left
        self.right = right
        return


class BST:
    def __init__(self, num_dims=2):
        self.root = None
        self.dims = num_dims
        return

    def insert(self, point):
        assert len(point) == self.dims
        self.root = self._insert(self.root, point, 0)
        return

    def _insert(self, node, point, dim):
        if node is None:
            return Node(point)

        if point[dim] < node.val[dim]:
            node.left = self._insert(node.left, point, (dim + 1) % self.dims)
        else:
            node.right = self._insert(node.right, point, (dim + 1) % self.dims)

        return node

    def count(self, x_l, y_l, x_r, y_r):
        return self._count(self.root, x_l, y_l, x_r, y_r, 0)

    def _count(self, node, x_l, y_l, x_r, y_r, dim):
        if node is None:
            return 0
        if x_l <= node.val[0] <= x_r and y_l <= node.val[1] <= y_r:
            count = 1
            count += self._count(node.left, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
            count += self._count(node.right, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
            return count
        else:
            if dim == 0:
                if node.val[0] < x_l:
                    return self._count(node.right, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                elif node.val[0] > x_r:
                    return self._count(node.left, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                else:
                    count = 0
                    count += self._count(node.left, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                    count += self._count(node.right, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                    return count
            else:
                if node.val[1] < y_l:
                    return self._count(node.right, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                elif node.val[1] > y_r:
                    return self._count(node.left, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                else:
                    count = 0
                    count += self._count(node.left, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                    count += self._count(node.right, x_l, y_l, x_r, y_r, (dim + 1) % self.dims)
                    return count


def num_qualify(first, second):
    treeObj = BST()
    points = list(zip(first, second))
    random.shuffle(points)
    for x, y in points:
        treeObj.insert((x, y))

    counts = list()
    for x, y in points:
        ltx = treeObj.count(0, 0, x, 1 + 10**9)
        lty = treeObj.count(0, 0, 1 + 10**9, y)
        ltxy = treeObj.count(0, 0, x, y)
        counts.append(ltx + lty - ltxy - 1)

    counter = Counter(counts)
    return counter.most_common(1)[0][1]


for _ in range(int(input())):
    n = int(input())
    a1 = map(int, input().strip().split(' '))
    a2 = map(int, input().strip().split(' '))

    print(num_qualify(a1, a2))
