def get_y(bin_string, n):
    for idx in range(1, n):
        if bin_string[idx] == '1':
            return idx

    return n


for _ in range(int(input())):
    n = int(input())
    bin_string = input()
    print(get_y(bin_string.lstrip('0'), n))
