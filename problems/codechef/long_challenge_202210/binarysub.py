M = 998244353


def get_count(final_string):
    n = len(final_string)
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for idx in range(2, n+1):
        edge_string = final_string[idx - 2:idx]
        if edge_string == 'aa' or edge_string == 'bb':
            dp[idx] = dp[idx - 1]
        else:
            dp[idx] = dp[idx - 2] * 2
        dp[idx] = dp[idx] % M
    # print(dp)
    return dp[n] % M


for _ in range(int(input())):
    s = input().strip()
    print(get_count(s))
