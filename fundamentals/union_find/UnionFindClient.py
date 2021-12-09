import random
import time

from QuickFind import QuickFind
from QuickUnion import QuickUnion
from QuickUnionWeighted import QuickUnionWeighted
from QuickUnionPathComp import QuickUnionPathComp
from QuickUnionWeightedPathComp import QuickUnionWeightedPathComp


def main(n, union_pairs, find_pairs):
    # obj = QuickFind(n)
    # obj = QuickUnion(n)
    # obj = QuickUnionWeighted(n)
    # obj = QuickUnionPathComp(n)
    obj = QuickUnionWeightedPathComp(n)

    t1 = time.time()
    # Fill the object
    for p, q in union_pairs:
        obj.union(p, q)

    # Query the object
    for p, q in find_pairs:
        _ = obj.connected(p, q)

    t2 = time.time()
    print(f"Time taken (sec): {t2 - t1}")

    # Size of trees
    # max_size = -1
    # for idx in range(n):
    #     if obj.size[idx] > max_size:
    #         max_size = obj.size[idx]
    #         print(idx, obj.size[idx])
    return


if __name__ == "__main__":
    n = 10**5
    u_pairs = list()
    for i in range(n):
        p = random.randint(0, n - 1)
        done = False
        while not done:
            q = random.randint(0, n - 1)
            if q != p:
                done = True
        u_pairs.append((p, q))
        # u_pairs.append((i, (i + 1) % n))

    f_pairs = list()
    for _ in range(n):
        p = random.randint(0, n - 1)
        done = False
        while not done:
            q = random.randint(0, n - 1)
            if q != p:
                done = True
        f_pairs.append((p, q))

    main(n, u_pairs, f_pairs)
