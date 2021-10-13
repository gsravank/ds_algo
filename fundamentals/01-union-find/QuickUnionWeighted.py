class QuickUnionWeighted:
    def __init__(self, n):
        self.items = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        return

    def root(self, p):
        while self.items[p] != p:
            p = self.items[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_of_p = self.root(p)
        root_of_q = self.root(q)

        if root_of_q == root_of_p:  # Bug if we don't check this!
            return

        if self.size[root_of_p] < self.size[root_of_q]:
            self.items[root_of_p] = root_of_q
            self.size[root_of_q] += self.size[root_of_p]
        else:
            self.items[root_of_q] = root_of_p
            self.size[root_of_p] += self.size[root_of_q]

        return
