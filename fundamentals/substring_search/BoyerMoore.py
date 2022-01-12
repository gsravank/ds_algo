import random
import string
from utils.DSUtils import get_array_print_string


class BoyerMoore:
    def __init__(self, alphabet=None):
        if alphabet is None:
            self.alphabet = string.ascii_lowercase
        else:
            self.alphabet = alphabet

        self.R = len(self.alphabet)
        self.key_to_index_map = dict(zip(self.alphabet, list(range(self.R))))
        return

    def _build_skip_table(self, pattern):
        right = [-1 for _ in range(self.R)]
        for idx, char in enumerate(pattern):
            right[self.key_to_index_map[char]] = idx
        return right

    def search(self, text, pattern, start):
        n = len(text)
        m = len(pattern)
        remaining = n - start
        if remaining < m:
            return -1

        right = self._build_skip_table(pattern)

        j = 0
        i = start
        while i <= n - m:
            skip = 0
            for j in range(m-1, -1, -1):
                print(get_array_print_string(text, [i, i + j]))
                print(get_array_print_string(' ' * i + pattern, [i + j]))
                print('\n')
                if pattern[j] == text[i + j]:
                    pass
                else:
                    skip = max(1, j - right[self.key_to_index_map[text[i + j]]])
                    print(f"Skip = {skip}")
                    break

            if skip == 0:
                return i
            else:
                i += skip

        return n


if __name__ == '__main__':
    pat = 'needle'
    txt = 'findinahaystackneedleina'

    alphabet = string.ascii_lowercase
    obj = BoyerMoore(alphabet)
    right = obj._build_skip_table(pat)
    print('\t'.join([str(x) for x in range(len(pat))]))
    print('\t'.join(pat) + '\n')
    print('\t'.join(alphabet))
    print('\t'.join([str(y) for y in right]))
    print('')

    print('\t'.join([str(x) for x in range(len(txt))]))
    print('\t'.join(txt))
    print('\n')
    match_idx = obj.search(txt, pat, 0)
    print(match_idx)
    if match_idx < len(txt):
        print(get_array_print_string(txt, [match_idx, match_idx + len(pat) - 1], True))
