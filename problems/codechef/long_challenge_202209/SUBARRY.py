def min_max_interesting(arr, n):
    arr = sorted(arr)

    maxValue = max(arr[0]*arr[0], arr[-1]*arr[-1])

    if arr[0] >= 0 or arr[-1] <= 0:
        minValue = min(arr[0]*arr[0], arr[-1]*arr[-1])
    else:
        minValue = arr[0] * arr[-1]
    return minValue, maxValue


for _ in range(int(input())):
    n = int(input())
    arr = map(int, input().strip().split(' '))

    a, b = min_max_interesting(arr, n)
    print(a, b)