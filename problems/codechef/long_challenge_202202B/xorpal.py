def check(array, sz):
    if sz % 2 == 1:
        return True
    else:
        counts = [0, 0]
        for num in array:
            counts[num] += 1
        if (counts[0] == counts[1]) or (counts[0] % 2 == 0 and counts[1] % 2 == 0):
            return True
        else:
            return False


for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().strip()]

    print("YES" if check(arr, n) else "NO")
