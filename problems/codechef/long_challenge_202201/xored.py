import math
from collections import defaultdict


def turn_on_bit(num, k):
    return num | 1 << k-1


def turn_off_bit(num, k):
    if k <= 0:
        return num

    return num & ~(1 << k-1)


def get_bin_from_num(num, k):
    ans = list()
    for _ in range(k):
        ans.append(num % 2)
        num = num // 2
    return ans


def f0(idx, n):
    num_ones = 2
    init = 0
    for k in range(num_ones):
        init = turn_on_bit(init, k + 1)

    if idx < n-1:
        init = init << idx
        return init
    else:
        init = init << n - 2
        init = turn_off_bit(init, n-1)
        init = turn_on_bit(init, 1)
        return init


def f1(n, idx):
    num_ones = 1
    init = 0
    for k in range(num_ones):
        init = turn_on_bit(init, k + 1)

    return init << idx


def get_numbers(n, x):
    if n == 1:
        return [x]
    elif n == 2:
        n1 = 0
        n2 = 0
        k = 1
        while x:
            if x % 2 == 0:
                n1 = turn_on_bit(n1, k)
                n2 = turn_on_bit(n2, k)
                # d1 = 1
                # d2 = 1
            else:
                n1 = turn_on_bit(n1, k)
                # d1 = 1
                # d2 = 0
            k += 1
            x = x // 2

        return [n1, n2]

    nums = [0 for _ in range(n)]
    counts = defaultdict(lambda : 0)
    
    num_iter = math.ceil(math.log2(n))
    num_digits = n
    print(num_digits, num_iter)
    for _ in range(num_iter):
        print(x)
        x_last = x % 2
        x = x // 2

        if x_last == 0:
            curr = f0(num_digits, counts[x_last])
        else:
            curr = f1(num_digits, counts[x_last])
        counts[x_last] += 1
        digits = get_bin_from_num(curr, num_digits)  # [::-1]

        for idx, digit in enumerate(digits):
            nums[idx] = (2 * nums[idx]) + digit

        # print(x_last, digits, nums)
        # print()

    return nums


# for idx in f0(3):
#     print(idx)

# for idx in f1(3):
#     print(idx)

for _ in range(int(input())):
    n, x = map(int, input().strip().split(' '))
    numbers = get_numbers(n, x)
    print(' '.join([str(y) for y in numbers]))
