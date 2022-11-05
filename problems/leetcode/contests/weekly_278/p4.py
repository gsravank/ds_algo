def isConnected(s1, s2):
    if abs(len(s2) - len(s1)) >= 2:
        return False

    c1 = 0
    for s in s1:
        if s not in s2:
            c1 += 1
    c2 = 0
    for s in s2:
        if s not in s1:
            c2 += 1
    print(c1, c2)
    if c1 >= 2 or c2 >= 2:
        return False

    return True


print(isConnected('abc', 'abyx'))