def xor(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a != b:
        return 1
    else:
        return 0


def print_xor(so_far, remaining, value):
    if remaining == 0:
        for x in so_far:
            print(x, end='')
        print(' ', end='')
        print(value)

        return

    print_xor(so_far[:] + [0], remaining - 1, xor(value, 0))
    print_xor(so_far[:] + [1], remaining - 1, xor(value, 1))

    return

print_xor([], 3, None)
