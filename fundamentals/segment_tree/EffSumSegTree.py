"""
https://codeforces.com/blog/entry/18051
"""


class EffSumSegmentTree:
    def __init__(self):
        self.n = 0
        self.tree = []

    def build(self, arr):
        self.n = len(arr)
        self.tree = [0 for _ in range(2 * self.n)]
        # Fill the leaves first
        for i in range(len(arr)):
            self.tree[i + self.n] = arr[i]

        # Fill all others from children
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

        return

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                ans += self.tree[r]
            l >>= 1
            r >>= 1
        return ans

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]