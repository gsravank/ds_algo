import random
import string
from utils.DSUtils import get_array_print_string


class KMPDFA:
    def __init__(self, alphabet=None):
        if alphabet is None:
            self.alphabet = string.ascii_lowercase
        else:
            self.alphabet = alphabet

        self.R = len(self.alphabet)
        self.key_to_index_map = dict(zip(self.alphabet, list(range(self.R))))
        return

    def _build_dfa_array_(self, pattern):
        n = len(pattern)
        dfa = [[0 for _ in range(n)] for _ in range(self.R)]

        dfa[self.key_to_index_map[pattern[0]]][0] = 1
        X = 0
        for j in range(1, n):
            for c in self.alphabet:
                dfa[self.key_to_index_map[c]][j] = dfa[self.key_to_index_map[c]][X]
            dfa[self.key_to_index_map[pattern[j]]][j] = j + 1
            X = dfa[self.key_to_index_map[pattern[j]]][X]

        return dfa

    def search(self, text, pattern, start):
        n = len(text)
        m = len(pattern)
        remaining = n - start
        if remaining < m:
            return -1

        dfa = self._build_dfa_array_(pattern)

        j = 0
        i = start
        while i < n:
            print(get_array_print_string(text, [i]))
            print(get_array_print_string(' ' * (i-j) + pattern, [i]))
            print('\n')
            j = dfa[self.key_to_index_map[text[i]]][j]
            i += 1

            if j == m:
                return i - m

        return n


if __name__ == '__main__':
    pat = 'aaaaba'
    txt = 'aaabaaabaaaaba'

    obj = KMPDFA('abc')
    dfa = obj._build_dfa_array_(pat)
    print('\t'.join([str(x) for x in range(len(pat))]))
    print('\t'.join(pat) + '\n')
    print('\n'.join(['\t'.join([str(y) for y in x]) for x in dfa]))
    print('')

    print('\t'.join([str(x) for x in range(len(txt))]))
    print('\t'.join(txt))
    print('\n')
    match_idx = obj.search(txt, pat, 0)
    print(match_idx)
    if match_idx < len(txt):
        print(get_array_print_string(txt, [match_idx, match_idx + len(pat) - 1], True))
