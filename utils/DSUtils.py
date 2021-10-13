import random


def print_2d_matrix(matrix, val_print_map=None, sep='\t', print_vertical_edges=False,
                    print_horizontal_edges=False):
    print_strings = list()

    max_len = -1
    for row in matrix:
        if val_print_map is None:
            curr_str = sep.join([str(item) for item in row])
        else:
            curr_str = sep.join([str(val_print_map[item]) if item in val_print_map else str(item) for item in row])

        if print_vertical_edges:
            curr_str = sep + curr_str + sep

        max_len = max(len(curr_str), max_len)
        print_strings.append(curr_str)

    if print_horizontal_edges:
        horizontal_line = '.' * max_len
        print('\n'.join([horizontal_line] + print_strings + [horizontal_line]))
    else:
        print('\n'.join(print_strings))
    return


if __name__ == "__main__":
    n = 10
    mat = list()
    for _ in range(n):
        curr_list = list()
        for _ in range(n):
            curr_list.append(random.randint(0, 1))
        mat.append(curr_list)

    print_2d_matrix(mat, None, ' | ', True, False)
