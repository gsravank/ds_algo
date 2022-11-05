def getpmod(k, m, p):
    fin = dict()
    curr = 1
    for idx in range(k):
        fin[idx] = curr
        curr = (curr * p) % m
    return fin

print(getpmod(7, 15, 7))
print(getpmod(7, 15, 3))
