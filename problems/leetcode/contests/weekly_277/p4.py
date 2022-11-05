import random


def create_truth_array(num, n):
    array = list()
    for _ in range(n):
        curr_truth = num % 2
        array.append(curr_truth)
        num = num // 2

    return array


def create_test_case(n):
    two_to_n = 2 ** n
    rand_truth_val = random.randint(0, two_to_n - 1)
    rand_truth_arr = create_truth_array(rand_truth_val, n)
    num_truth = sum(rand_truth_arr)

    statements = []
    for idx in range(n):
        if rand_truth_arr[idx] == 1:
            statements.append(rand_truth_arr[:])
        else:
            curr_list = list()
            for _ in range(n):
                curr_list.append(random.randint(0, 1))
            statements.append(curr_list)
        statements[idx][idx] = 2

    return statements, num_truth, rand_truth_arr


n = 15
statements, num_truth, truth_arr = create_test_case(n)
print(num_truth)
print(truth_arr)
print(statements)