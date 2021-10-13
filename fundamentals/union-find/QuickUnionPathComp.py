class QuickUnionPathComp:
    def __init__(self, n):
        self.items = [i for i in range(n)]

    def root(self, p):
        while p != self.items[p]:
            # This is the only extra line. Understand it!
            # We are halving the path length
            # Point every other node in the path point to its grandparent
            self.items[p] = self.items[self.items[p]]
            p = self.items[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_of_p = self.root(p)
        root_of_q = self.root(q)

        # Set root of p to be child of root of q
        self.items[root_of_p] = root_of_q
        return
