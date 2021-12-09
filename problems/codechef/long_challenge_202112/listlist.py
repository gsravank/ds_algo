from collections import Counter


def compute_min_operations(num_items, integers):
    if num_items == 1:
        return 0

    counter = Counter(integers)
    most_common_info = counter.most_common(1)[0]

    most_common_item = most_common_info[0]
    most_common_freq = most_common_info[1]

    if most_common_freq == 1:
        return -1
    if most_common_freq == num_items:
        return 0

    remaining_count = num_items - most_common_freq

    return remaining_count + 1


for _ in range(int(input())):
    N = int(input())
    array = list(map(int, input().strip().split(' ')))

    print(compute_min_operations(N, array))
