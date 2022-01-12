import random
import string
from utils.DSUtils import get_array_print_string


class RabinKarp:
    def __init__(self, alphabet=None, Q=None):
        if alphabet is None:
            self.alphabet = string.ascii_lowercase
        else:
            self.alphabet = alphabet

        if Q is None:
            self.Q = 997

        self.R = len(self.alphabet)
        self.key_to_index_map = dict(zip(self.alphabet, list(range(self.R))))

        self.RM = 1
        return

    def compute_rm(self, m):
        self.RM = 1
        for _ in range(m - 1):
            self.RM = (self.RM * self.R) % self.Q

        return

    def compute_hash(self, text, m):
        hash_value = 0

        for i in range(m):
            char = text[i]
            idx = self.key_to_index_map[char]
            hash_value = ((hash_value * self.R) + idx) % self.Q

        return hash_value

    def search(self, text, pattern):
        n = len(text)
        m = len(pattern)
        if n < m:
            return n

        self.compute_rm(m)
        pat_hash = self.compute_hash(pattern, m)
        text_hash = self.compute_hash(text, m)

        if pat_hash == text_hash:
            return 0

        print(get_array_print_string(text, [0, m-1]))
        print(f"Hash = {text_hash}")
        print('\n')

        for idx in range(m, n):
            text_hash = (text_hash + self.Q - ((self.key_to_index_map[text[idx - m]] * self.RM) % self.Q)) % self.Q
            text_hash = (text_hash * self.R + self.key_to_index_map[text[idx]]) % self.Q

            print(get_array_print_string(text, [idx - m + 1, idx]))
            print(f"Hash = {text_hash}")
            print('\n')

            if text_hash == pat_hash:
                return idx - m + 1

        return n


if __name__ == '__main__':
    pat = 'needle'
    txt = 'findinahaystackneedleina'

    # pat = 'aaaaa'
    # txt = 'aaaabaaaabaaaabaaaaa'

    alphabet = string.ascii_lowercase
    obj = RabinKarp(alphabet)
    pat_hash = obj.compute_hash(pat, len(pat))
    print('\t'.join([str(x) for x in range(len(pat))]))
    print('\t'.join(pat))
    print('\t'.join([str(obj.key_to_index_map[x]) for x in pat]))
    print(f'Pat Hash: {pat_hash}')
    print(f'R = {obj.R}')
    print(f'Q = {obj.Q}')
    print('')

    print('\t'.join([str(x) for x in range(len(txt))]))
    print('\t'.join(txt))
    print('\n')
    match_idx = obj.search(txt, pat)
    print(match_idx)
    if match_idx < len(txt):
        print(get_array_print_string(txt, [match_idx, match_idx + len(pat) - 1], True))
