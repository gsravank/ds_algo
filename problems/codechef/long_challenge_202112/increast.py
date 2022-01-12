import string
from collections import defaultdict


ALPHABETS = string.ascii_lowercase


def get_next_curr_alphabet_idx(curr_alphabet_idx, positions, curr_str_idx):
    done = False
    while not done:
        if len(positions[ALPHABETS[curr_alphabet_idx]]) == 0 or positions[ALPHABETS[curr_alphabet_idx]][-1] < curr_str_idx:
            curr_alphabet_idx += 1
            if curr_alphabet_idx == len(ALPHABETS):
                return curr_alphabet_idx
        else:
            done = True
    return curr_alphabet_idx


def get_min_string(s):
    left_indices = defaultdict(lambda : False)
    positions = defaultdict(lambda : list())
    for idx in range(len(s)):
        positions[s[idx]].append(idx)

    curr_alphabet_idx = 0
    first_alphabet = s[0]
    done_with_first = False
    for curr_str_idx in range(len(s)):
        curr_alphabet_idx = get_next_curr_alphabet_idx(curr_alphabet_idx, positions, curr_str_idx)
        # print(curr_str_idx, s[curr_str_idx], curr_alphabet_idx, ALPHABETS[curr_alphabet_idx], done_with_first)
        if curr_alphabet_idx == len(ALPHABETS):
            break
        curr_alphabet = ALPHABETS[curr_alphabet_idx]

        if done_with_first and curr_alphabet > first_alphabet:
            break

        if s[curr_str_idx] == curr_alphabet:
            left_indices[curr_str_idx] = True
        else:
            if not done_with_first:
                first_alphabet = s[curr_str_idx]
                done_with_first = True

    fin_string = ''.join([s[idx] for idx in range(len(s)) if left_indices[idx]]) + ''.join([s[idx] for idx in range(len(s)) if not left_indices[idx]])
    return fin_string

#import random
# _x = 'aaxbcdadaa'
# _x = random.choices(ALPHABETS, k=10)
# _y = get_min_string(_x)
# print(_x)
# print(_y)

# print(get_min_string('aba'))
# print(get_min_string('abcd'))
# print(get_min_string('cbcdbef'))
# print(get_min_string('fabcdac'))
# print(get_min_string('fggggeadddadddbaxxxbghij'))


for _ in range(int(input())):
    s = input().strip()
    print(get_min_string(s))

# import random
# from tqdm import tqdm
# for idx in tqdm(range(10**5)):
#     n = random.randint(1, 10**2)
#     curr_string = ''.join(random.choices(ALPHABETS, k=n))
#
#     if idx <= 5:
#         print(n)
#         print(curr_string)
#
#     try:
#         ret_string = get_min_string(curr_string)
#         if len(ret_string) != len(curr_string):
#             print(curr_string)
#     except Exception as e:
#         print(curr_string)
#         print(e.__str__())
#         print('\n')
#