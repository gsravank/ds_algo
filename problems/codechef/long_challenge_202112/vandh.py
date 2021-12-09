def create_bin_string(nh, nv):
    # h = 010
    # v = 101
    if nh == nv:
        return ''.join(['10' for _ in range(nh + 1)])
    elif nh > nv:
        base_string = ''.join(['01' for _ in range(nv + 1)])
        support_string = '0'
        remaining_string = ''.join(['010' for _ in range(nh - nv - 1)])
        return base_string + support_string + remaining_string
    else:
        base_string = ''.join(['10' for _ in range(nh + 1)])
        support_string = '1'
        remaining_string = ''.join(['101' for _ in range(nv - nh - 1)])
        return base_string + support_string + remaining_string


for _ in range(int(input())):
    n, m = list(map(int, input().strip().split(' ')))
    bin_string = create_bin_string(n, m)
    print(len(bin_string))
    print(bin_string)
