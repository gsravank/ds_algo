class QuickFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]

    def connected(self, p, q):
        assert p < len(self.id) and q < len(self.id)
        return self.id[p] == self.id[q]

    def union(self, p, q):
        assert p < len(self.id) and q < len(self.id)
        pid = self.id[p]  # Need to get pid and qid first. Else it could turn out to be a major bug
        qid = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
        return
