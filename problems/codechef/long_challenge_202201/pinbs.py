def remove_left_zeros(string):
    for idx, char in enumerate(string):
        if char == '1':
            break
    return string[idx:]


for _ in range(int(input())):
    s = remove_left_zeros(input().strip())
    # print(f"'{s}'")
    n = len(s)

    if n <= 1:
        print("No")
    else:
        print("Yes")