def get_primes_leq(n):
    # array of type boolean with True values in it
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If it remain unchanged it is prime
        if (prime[p] == True):
            # updating all the multiples
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return [idx for idx in range(n + 1) if prime[idx]]


def get_max_distinct(n, primes):
    if n <= 2:
        return 1
    left, right = 0, len(primes) - 1
    ans = None
    while left <= right:
        mid = (left + right) // 2
        if primes[mid] > n:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

MAX_N = 10**9
primes = get_primes_leq(MAX_N)

for _ in range(int(input())):
    n = int(input().strip())
    print(get_max_distinct(n, primes))
