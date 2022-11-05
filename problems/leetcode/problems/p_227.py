def getPieces(s):
    opIds = [-1]
    ops = set(['+', '-', '*', '/'])
    for idx, ch in enumerate(s):
        if ch in ops:
            opIds.append(idx)
    opIds.append(len(s))

    pieces = list()
    for first, second in zip(opIds[:-1], opIds[1:]):
        pieces.append(s[first + 1:second])
        if second < len(s):
            pieces.append(s[second])
    return pieces

print(getPieces('22+3/2-5*100-5/4'))