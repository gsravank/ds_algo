def canConvertToPalindrome(binString, n, k):
    start = 0
    end = n - 1
    count = 0
    while start < end:
        if binString[start] != binString[end]:
            count += 1
        start += 1
        end -= 1

    if n % 2 == 0:
        return count <= k and (k - count) % 2 == 0
    else:
        return count <= k


for _ in range(int(input())):
    n, k = map(int, input().strip().split(' '))
    binStr = input().strip()
    print("YES" if canConvertToPalindrome(binStr, n, k) else "NO")
