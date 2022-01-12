from utils.DSUtils import get_array_print_string


def build(pat):
    m = len(pat)
    nfa = [0 for _ in range(m)]
    j = 0 # virtual state run through nfa
    for i in range(1,m):
        nfa[i] = j
        while j > 0 and pat[i] != pat[j]:
            j = nfa[j]
        if pat[i] == pat[j]:
            j += 1
    return nfa


def match(txt, pat):
    n = len(txt)
    m = len(pat)
    nfa = build(pat)

    j = 0 # match state
    for i in range(n):
        print(get_array_print_string(txt, [i]))
        print(get_array_print_string(' ' * (i - j) + pat, [i]))
        print('\n')
        while j > 0 and txt[i] != pat[j]:
            j = nfa[j]
            print('-')
            print(get_array_print_string(txt, [i]))
            print(get_array_print_string(' ' * (i - j) + pat, [i]))
            print('\n')
        if txt[i] == pat[j]:
            j += 1
        if j >= m:
            return i-m+1
    return -1


if __name__ == '__main__':
    pattern = 'aaaaa'
    txt = 'aaaabaaaabaaaabaaaaa'
    m = len(pattern)
    nfa = build(pattern)

    print('\t'.join([str(x) for x in range(m)]))
    print(f'\t'.join(pattern))
    print('\t'.join([str(x) for x in nfa]))

    print('\t'.join([str(x) for x in range(len(txt))]))
    print('\t'.join(txt))
    print('\n')
    match_idx = match(txt, pattern)
    print(match_idx)
    print(get_array_print_string(txt, [match_idx, match_idx + len(pattern) - 1], True))
