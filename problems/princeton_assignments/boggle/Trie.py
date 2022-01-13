from utils.GenUtils import read_lines


class Node:
    def __init__(self):
        self.next = dict()
        self.val = 0
        return


class Trie:
    def __init__(self, words):
        self.root = Node()

        for word in words:
            self.insert_word(word.replace("QU", "Q"))
        return

    def insert_word(self, word):
        m = len(word)
        self.root = self._insert_word(self.root, word, 0, m)
        return

    def _insert_word(self, root, word, digit, word_len):
        if root is None:
            root = Node()

        if digit == word_len:
            root.val = 1
        else:
            if word[digit] not in root.next:
                root.next[word[digit]] = None
            root.next[word[digit]] = self._insert_word(root.next[word[digit]], word, digit + 1, word_len)
        return root

    def is_present(self, word):
        word = word.replace("QU", "Q")
        curr_node = self.root

        for char in word:
            if char in curr_node.next:
                curr_node = curr_node.next[char]
            else:
                return False

        return curr_node.val == 1


if __name__ == "__main__":
    words = ['a', 'abc', 'abcdef', 'b', 'bef']
    words = read_lines('/Users/sravan/Projects/ds_algo/problems/princeton_assignments/boggle/data/dictionary-algs4.txt')
    trie = Trie(words)
    test_words = ['a', 'ab', 'abc', 'abcd', 'abcdef', 'abcdefg', 'bc']
    test_words = words
    for word in test_words:
        if not trie.is_present(word):
            print(word)
        # print(f"{word}: {trie.is_present(word)}")
