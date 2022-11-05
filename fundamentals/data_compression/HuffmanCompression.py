from heapq import heappush, heapify, heappop
from collections import Counter


class Node:
    def __init__(self, char='0', freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        return

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


class HuffmanEncoding:
    def __init__(self, text):
        self.text = text

        self.trie = self._build_trie()
        self.encoding_map, self.decoding_map = self._get_encoding_map()

        return

    def _build_trie(self):
        freq_map = Counter(self.text)
        # print(freq_map)
        char_nodes = [Node(char, freq) for char, freq in freq_map.items()]
        heapify(char_nodes)

        for _ in range(len(char_nodes) - 1):
            min_first = heappop(char_nodes)
            min_second = heappop(char_nodes)

            # Merge these two nodes
            new_node = Node('0', min_first.freq + min_second.freq, min_first, min_second)

            # Push new_node into priority queue
            heappush(char_nodes, new_node)

        return char_nodes[0]

    def _get_encoding_map(self):
        encoding_map = dict()
        decoding_map = dict()

        # Traverse the trie
        digits_so_far = list()
        self._traverse(self.trie, digits_so_far, encoding_map, decoding_map)

        return encoding_map, decoding_map

    def _traverse(self, node, digits_so_far, encoding_map, decoding_map):
        # Note down digits as you traverse
        # When you reach a leaf, store sequence of digits as code for the character
        if node.is_leaf():
            encoding_map[node.char] = ''.join(digits_so_far)
            decoding_map[''.join(digits_so_far)] = node.char
        else:
            digits_so_far.append('0')
            self._traverse(node.left, digits_so_far, encoding_map, decoding_map)
            digits_so_far.pop()
            digits_so_far.append('1')
            self._traverse(node.right, digits_so_far, encoding_map, decoding_map)
            digits_so_far.pop()

        return

    def get_encoding(self, sep=''):
        encoding_strings = list()
        for char in self.text:
            encoding_strings.append(self.encoding_map[char])

        return sep.join(encoding_strings)

    def get_decoding(self, encoded_text):
        decoded_strings = list()
        n = len(encoded_text)
        start = 0
        for end in range(n):
            curr_string = encoded_text[start: end + 1]
            if curr_string in self.decoding_map:
                decoded_strings.append(self.decoding_map[curr_string])
                start = end + 1

        return ''.join(decoded_strings)


if __name__ == '__main__':
    text = 'abracadabra!'
    print(text)

    hc = HuffmanEncoding(text)
    print(hc.encoding_map)
    print(hc.decoding_map)
    encoding = hc.get_encoding('|')
    print(hc.get_encoding('|'))
    decoding = hc.get_decoding(encoding.replace("|", ""))
    print(decoding)
