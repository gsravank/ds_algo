def get_min_ops(array, sz):
    diff = 0
    count = 0
    for i, num in enumerate(array):
        idx = i + 1
        if num - idx == diff:
            diff += 1
            count += 1

    return count


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))

    print(get_min_ops(arr, n))
