def get_winning_array(moves, n):
    if n == 1:
        return [moves]
    next_r = [None for _ in range(n)]
    next_s = [None for _ in range(n)]
    next_p = [None for _ in range(n)]

    latest_r = None
    latest_s = None
    latest_p = None
    for idx in range(n-1, -1, -1):
        next_r[idx] = latest_r
        next_s[idx] = latest_s
        next_p[idx] = latest_p

        if moves[idx] == 'R':
            latest_r = idx
        elif moves[idx] == 'S':
            latest_s = idx
        else:
            latest_p = idx

    # print('Next P', next_p)
    # print('Next R', next_r)
    # print('Next S', next_s)
    winning_array = [None for _ in range(n)]
    winning_array[-1] = moves[-1]
    for idx in range(n-2, -1, -1):
        curr_move = moves[idx]
        if curr_move == 'R':
            if next_p[idx] is None:
                winning_array[idx] = 'R'
            else:
                winning_array[idx] = winning_array[next_p[idx]]
        elif curr_move == 'S':
            if next_r[idx] is None:
                winning_array[idx] = 'S'
            else:
                winning_array[idx] = winning_array[next_r[idx]]
        else:
            if next_s[idx] is None:
                winning_array[idx] = 'P'
            else:
                winning_array[idx] = winning_array[next_s[idx]]

    return winning_array


for _ in range(int(input())):
    N = int(input())
    moves = input().strip()

    w_array = get_winning_array(moves, N)
    print(''.join(w_array))
