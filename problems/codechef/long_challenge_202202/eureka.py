def get_nearest(n):
    ans = (0.143 * n)
    ans = ans ** n

    ans_ = int(ans) * 1.0

    if abs(ans - ans_) < 0.5:
        return int(ans_)
    else:
        return int(ans_) + 1


for _ in range(int(input())):
    n = int(input())
    print(get_nearest(n))
    
