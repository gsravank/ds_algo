def gcd_possible(array, sz, m, gcd):
    amount_to_sub = 0
    mults_available = 0
    for num in array:
        curr_mult, rem = divmod(num, gcd)
        mults_available += curr_mult
        amount_to_sub += rem

        if amount_to_sub > m:
            return False

    diff = m - amount_to_sub
    diff_mult, diff_rem = divmod(diff, gcd)
    # print(m, amount_to_sub, mults_available)
    # print(diff_mult, diff_rem)
    if diff_rem == 0 and diff_mult < mults_available:
        return True
    else:
        return False


def get_max_gcd(array, sz, m):
    max_elem = max(array)
    for gcd in range(max_elem, 0, -1):
        # print(gcd, end=' ')
        if gcd_possible(array, sz, m, gcd):
            # print()
            return gcd

    return

flag = False
if flag:
    print(gcd_possible([1,3,5,7], 4, 4, 1))
else:
    for _ in range(int(input())):
        n, m = input().strip().split(' ')
        arr = list(map(int, input().strip().split(' ')))
        print(get_max_gcd(arr, int(n), int(m)))