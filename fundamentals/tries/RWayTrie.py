import random
import string


class Node:
    def __init__(self, R):
        self.val = None
        self.next = [None for _ in range(R)]
        return


class RWayTrie:
    def __init__(self, sorted_keys=None):
        if sorted_keys is None:
            sorted_keys = string.ascii_lowercase

        self.R = len(sorted_keys)
        self.key_to_index_map = dict(zip(sorted_keys, list(range(self.R))))

        self.root = Node(self.R)

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)
        return

    def _put(self, root, key, val, digit):
        if root is None:
            root = Node(self.R)

        if digit == len(key):
            root.val = val
            return root

        char = key[digit]
        root.next[self.key_to_index_map[char]] = self._put(root.next[self.key_to_index_map[char]], key, val, digit + 1)

        return root

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        node = self._get(self.root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, root, key, digit):
        if root is None:
            return None

        if digit == len(key):
            return root

        char = key[digit]

        return self._get(root.next[self.key_to_index_map[char]], key, digit + 1)


if __name__ == '__main__':
    obj = RWayTrie()

    alphabet = 'abc'
    str_len = 5
    words = list()
    for _ in range(20):
        curr_word = ''.join(random.choices(alphabet, k=random.randint(1, str_len)))
        if obj.contains(curr_word):
            print(f"{curr_word} is already in the trie")
        else:
            print(f"Inserting {curr_word}")
        obj.put(curr_word, 1)
        words.append(curr_word)
    print(len(set(words)))

    num_twos = 0
    for word in words:
        if random.random() <= 0.5:
            obj.put(word, 2)
            num_twos += 1

    for word in words:
        print(f"{word} {obj.contains(word)} {obj.get(word)}")

    print(f'\nNum twos: {num_twos}')