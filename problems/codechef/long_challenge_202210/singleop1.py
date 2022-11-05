def get_y(bin_string, n):
    for idx in range(n):
        if bin_string[idx] == '0':
            return idx

    return n


for _ in range(int(input())):
    n = int(input())
    bin_string = input()
    print(get_y(bin_string.lstrip('0'), n))
