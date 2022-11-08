class Trie:
    def __init__(self, words=[], endCh='#'):
        self.trie = dict()
        self._end = endCh
        for word in words:
            self.insert(word)
        return

    def insert(self, key, val=-1):
        t = self.trie
        for ch in key:
            if ch not in t:
                t[ch] = dict()
            t = t[ch]

        t[self._end] = val
        return

    def put(self, key, val):
        self.insert(key, val)

    def get(self, key):
        t = self.trie

        for ch in key:
            if ch not in t:
                return False
            else:
                t = t[ch]

        return t.get(self._end, None)

    def contains(self, key):
        return self.get(key) is not None

    def startsWith(self, prefix):
        t = self.trie

        for ch in prefix:
            if ch not in t:
                return False
            else:
                t = t[ch]
        return True

    def remove(self, word):
        t = self.trie
        path = list()
        for ch in word:
            if ch not in t:
                return
            t = t[ch]
            path.append((ch, t))

        if self._end in t:
            p = self._end
            for parent, currNode in path[::-1]:
                if p == self._end or len(currNode[p]) == 0:
                    del currNode[p]
                    p = parent
                else:
                    break

        return

    def removeRec(self, word):
        self._remove(word, self.trie)
        return

    def _remove(self, word, node, idx=0):
        if idx == len(word):
            if self._end in node:
                del node[self._end]
                return len(node) == 0
            else:
                return False
        else:
            if word[idx] in node and self._remove(word, node[word[idx]], idx + 1):
                if len(node[word[idx]]) == 0:
                    del node[word[idx]]
                    return True
                else:
                    return False
            else:
                return False


