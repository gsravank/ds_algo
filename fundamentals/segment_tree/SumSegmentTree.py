class SumSegmentTree:
    def __init__(self, tsi=0):
        self.n = 0
        self.tree = []
        self.arr = []
        assert tsi == 0 or tsi == 1
        self.tsi = tsi
        return

    def initialize(self, arr):
        self.n = len(arr)
        self.tree = [0 for _ in range(4*self.n)]
        self.arr = arr
        return

    def build(self, arr):
        self.initialize(arr)
        self._build(self.tsi, 0, self.n-1)
        return

    def lc(self, idx):
        if self.tsi == 0:
            return 2 * idx + 1
        else:
            return 2 * idx

    def rc(self, idx):
        if self.tsi == 1:
            return 2*idx + 2
        else:
            return 2*idx + 1
    
    def _build(self, nodeIdx, start, end):
        # print(nodeIdx, start, end)
        if start == end:
            self.tree[nodeIdx] = self.arr[start]
        else:
            mid = (start + end) // 2
            self._build(self.lc(nodeIdx), start, mid)
            self._build(self.rc(nodeIdx), mid + 1, end)
            self.tree[nodeIdx] = self.tree[self.lc(nodeIdx)] + self.tree[self.rc(nodeIdx)]
        return

    def query(self, l, r):
        return self._query(self.tsi, 0, self.n-1, l, r)

    def _query(self, nodeIdx, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[nodeIdx]
        mid = (start + end) // 2
        lVal = self._query(self.lc(nodeIdx), start, mid, l, r)
        rVal = self._query(self.rc(nodeIdx), mid+1, end, l, r)
        return lVal + rVal

    def modify(self, idx, newVal):
        diff = newVal - self.arr[idx]
        self._modify(self.tsi, 0, self.n-1, idx, diff)
        return

    def _modify(self, nodeIdx, start, end, idx, diff):
        if start == end:
            self.arr[idx] += diff
            self.tree[nodeIdx] += diff
        else:
            mid = (start + end) // 2
            self._modify(self.lc(nodeIdx), start, mid, idx, diff)
            self._modify(self.rc(nodeIdx), mid + 1, end, idx, diff)
            self.tree[nodeIdx] = self.tree[self.lc(nodeIdx)] + self.tree[self.rc(nodeIdx)]
        return
