def create_opp_parities(start, n):
    answer = [start]
    for _ in range(n-1):
        start = 1-start
        answer.append(start)
    return answer


def convert_to_parity(orig_list, fin_list):
    if orig_list == fin_list:
        return []
    if sum(orig_list) == 0:
        return None

    one_indexes = [idx for idx in range(len(orig_list)) if orig_list[idx] == 1]
    new_one_indexes = list()
    first_one_index = one_indexes[0]
    steps = list()

    for idx in range(len(orig_list)):
        if idx == first_one_index:
            continue

        orig_val = orig_list[idx]
        fin_val = fin_list[idx]

        if orig_val != fin_val:
            steps.append([idx + 1, first_one_index + 1])

        if fin_val == 1:
            new_one_indexes.append(idx)

    if orig_list[first_one_index] != fin_list[first_one_index]:
        if len(new_one_indexes) == 0:
            return None
        else:
            steps.append([first_one_index + 1, new_one_indexes[0] + 1])

    return steps


def get_steps(a, n):
    a_list = [x % 2 for x in a]
    zero_list = create_opp_parities(0, n)
    one_list = create_opp_parities(1, n)

    zero_ans = convert_to_parity(a_list, zero_list)
    one_ans = convert_to_parity(a_list, one_list)


    # print(a_list)
    # print(zero_list)
    # print(one_list)
    # print(zero_ans)
    # print(one_ans)
    # print('\n')

    if zero_ans is None and one_ans is None:
        return None
    elif zero_ans is None:
        return one_ans
    elif one_ans is None:
        return zero_ans
    else:
        if len(zero_ans) < len(one_ans):
            return zero_ans
        else:
            return one_ans


for _ in range(int(input())):
    n = int(input())
    a = map(int, input().strip().split(' '))

    steps = get_steps(a, n)

    if steps is None:
        print(-1)
    else:
        print(len(steps))
        for step in steps:
            print(f"{step[0]} {step[1]}")
