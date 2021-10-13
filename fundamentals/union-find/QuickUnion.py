class QuickUnion:
    def __init__(self, n):
        self.items = [i for i in range(n)]

    def root(self, p):
        while self.items[p] != p:
            p = self.items[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # Make p's root a child of q's root
        root_of_p = self.root(p)
        root_of_q = self.root(q)

        self.items[root_of_p] = root_of_q
