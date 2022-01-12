import random
from utils.DSUtils import get_array_print_string


class KMP:
    def __init__(self):
        return

    @staticmethod
    def _get_lps_array(string):
        n = len(string)
        lps = [0 for _ in range(n)]

        for i in range(1, n):
            j = lps[i-1]

            while j > 0 and string[i] != string[j]:
                j = lps[j - 1]

            if string[i] == string[j]:
                lps[i] = j + 1
            else:
                lps[i] = 0

        return lps

    @staticmethod
    def search(text, pattern, start):
        n = len(text)
        m = len(pattern)
        remaining = n - start
        if remaining < m:
            return -1

        lps = KMP._get_lps_array(pattern)

        j = 0
        i = start
        while i < n:
            print(get_array_print_string(text, [i]))
            print(get_array_print_string(' ' * (i-j) + pattern, [i]))
            print('\n')
            if text[i] == pattern[j]:
                j += 1
                i += 1
                if j == m:
                    return i - m
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

        return -1


if __name__ == '__main__':
    pat = 'aaaaa'
    txt = 'aaaabaaaabaaaaab'

    obj = KMP()
    lps = obj._get_lps_array(pat)
    print(' '.join(pat))
    print(' '.join([str(x) for x in lps]))
    print('')

    print('\t'.join([str(x) for x in range(len(txt))]))
    print('\t'.join(txt))
    print('\n')
    match_idx = obj.search(txt, pat, 0)
    print(match_idx)
    print(get_array_print_string(txt, [match_idx, match_idx + len(pat) - 1], True))
