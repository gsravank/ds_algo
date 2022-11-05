import math


def is_sorted(array, sz):
    if sz == 1:
        return True
    for idx in range(sz - 1):
        if array[idx] > array[idx + 1]:
            return False

    return True


def can_sort(array, sz):
    if is_sorted(array, sz):
        return True

    parent = list(range(sz))
    def union(i, j):
        parent[find(j)] = find(i)
        return
    def find(i):
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

    max_digits = int(math.log2(max(array))) + 1
    arr_copy = array[:]
    for dig in range(max_digits):
        first_idx = None
        for idx in range(sz):
            num = arr_copy[idx]
            if num % 2 == 1:
                if first_idx is None:
                    first_idx = idx
                else:
                    union(first_idx, idx)
            arr_copy[idx] = num // 2

    array_indices = [(num, idx) for idx, num in enumerate(array)]
    sorted_array_indices = sorted(array_indices)

    # print(array_indices)
    # print(sorted_array_indices)

    for orig, fin in zip(array_indices, sorted_array_indices):
        if find(orig[1]) != find(fin[1]):
            return False

    return True


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))

    print("Yes" if can_sort(arr, n) else "No")

# import random
# # random.seed(0)
# n = 20
# arr = [1]
# for _ in range(n-1):
#     arr.append(arr[-1] * 2)
# random.shuffle(arr)
# print(arr)
# print(can_sort(arr, n))