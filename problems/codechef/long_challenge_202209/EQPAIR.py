from collections import Counter


def good_pairs(arr, n):
    counter = Counter(arr)
    answer = 0
    for key, val in counter.items():
        if val > 1:
            answer += int(val * (val - 1) / 2)
    return answer


for _ in range(int(input())):
    n = int(input())
    arr = map(int, input().strip().split(' '))

    print(good_pairs(arr, n))
