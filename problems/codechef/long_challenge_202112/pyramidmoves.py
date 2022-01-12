import math

BIG_NUMBER = 7 + 10**9
factorial = dict()
factorial[0] = 1
for i in range(1, 200000):
    factorial[i] = (factorial[i - 1] * i) % BIG_NUMBER


def get_first_element(row):
    return 1 + (row * (row - 1) / 2)


def get_last_element(row):
    return row * (row + 1) / 2


def is_in_row(number, row):
    if row < 1:
        return False
    elif row == 1:
        return number == 1

    row_start = (row * (row - 1) / 2) + 1
    row_end = row * (row + 1) / 2

    return row_start <= number <= row_end


def get_row_number(number):
    if number == 1:
        return 1
    elif number <= 3:
        return 2

    temp_float = math.sqrt(2.0 * number)
    temp_int = int(temp_float)

    # possible_rows = [temp_int - 1, temp_int, temp_int + 1]
    possible_rows = [temp_int, temp_int + 1]
    for row in possible_rows:
        if is_in_row(number, row):
            return row
    return temp_int


def get_width_from_center(number, row):
    middle = (float(get_first_element(row)) + float(get_last_element(row))) / 2.0
    return middle - float(number)


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % p

        y = int(y / 2)
        x = (x * x) % p
    return res


def mod_inverse(n, p):
    return power(n, p-2, p)


def num_combinations(n, r, p):
    return ((factorial[n] * mod_inverse(factorial[r], p)) % p) * (mod_inverse(factorial[n - r], p) % p) % p


def compute_num_paths(start, end):
    if start >= end:
        return 0
    
    start_row = get_row_number(start)
    end_row = get_row_number(end)

    height_diff = end_row - start_row
    if height_diff <= 0:
        return 0

    start_width = get_width_from_center(start, start_row)
    end_width = get_width_from_center(end, end_row)
    width_diff = int(math.fabs(2.0 * (end_width - start_width)))

    if width_diff > height_diff:
        return 0
    if width_diff == height_diff:
        return 1

    num_lefts = int((height_diff + width_diff) / 2.0)
    num_rights = int((height_diff - width_diff) / 2.0)
    
    return num_combinations(height_diff, num_lefts, BIG_NUMBER)


for _ in range(int(input())):
    s, e = list(map(int, input().strip().split(' ')))
    print(compute_num_paths(s, e))

# from tqdm import tqdm
# row_numbers = [get_row_number(x) for x in tqdm(range(1, 2001 * 1000 + 1))]
# from collections import Counter
# counter = Counter(row_numbers)
#
# for key, val in counter.items():
#     if key != val:
#         print(key, val)