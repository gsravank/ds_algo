def find_max_sub_array_common_in_overlap(array_one, array_two, start_one, start_two):
    l_one, l_two = len(array_one), len(array_two)
    end_one, end_two = start_one + l_one - 1, start_two + l_two - 1

    if start_one < start_two and end_one < start_two:
        return 0
    if start_one > start_two and start_one > end_two:
        return 0

    # Three cases
    # Left overlap
    if start_one <= start_two:
        i1 = start_two - start_one
        j1 = l_one - 1
        i2 = 0
    else:
        if end_one <= end_two:
            i1 = 0
            j1 = l_one - 1
            i2 = start_one - start_two
        else:
            i1 = 0
            j1 = l_one - 1 - (end_one - end_two)
            i2 = start_one - start_two
    j2 = i2 + (j1 - i1)
    max_length = 0
    curr_length = 0
    for idx, jdx in zip(range(i1, j1 + 1), range(i2, j2 + 1)):
        # comparison of overlap pieces here
        if array_one[idx] == array_two[jdx]:
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:
            curr_length = 0

    return max_length


def compare_all_sub_arrays(array_one, array_two):
    if len(array_one) > len(array_two):
        array_one, array_two = array_two, array_one

    l_one, l_two = len(array_one), len(array_two)
    start_two = l_one

    max_length = 0
    for start_one in range(1, l_one + l_two):
        max_length = max(max_length, find_max_sub_array_common_in_overlap(array_one, array_two, start_one, start_two))

    return max_length


a1 = [1,4,5,3,2,1,7]
a2 = [3,2,1,7,8]

print(compare_all_sub_arrays(a1, a2))