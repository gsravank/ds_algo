import math
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


def get_array_print_string(array, indices_to_point=None, print_indices=False):
    idx_string = '\t'.join([str(idx) for idx in range(len(array))])
    elem_string = '\t'.join([str(elem) for elem in array])
    ptr_string = '\t'.join(['|' if indices_to_point is not None and idx in indices_to_point else ' '
                            for idx in range(len(array))])
    if print_indices:
        return '\n'.join([idx_string, elem_string, ptr_string])
    else:
        return '\n'.join([elem_string, ptr_string])


def is_sorted(array, start=None, end=None):
    if len(array) == 0:
        return True

    if start is None:
        start = 0
    else:
        assert 0 <= start <= len(array) - 1, "Provide start index between 0 and len(array) - 1"
    if end is None:
        end = len(array) - 1
    else:
        assert 0 <= end <= len(array) - 1, "Provide end index between 0 and len(array) - 1"

    assert start <= end, "Provide start less than end"

    for idx in range(start, end):
        if array[idx] > array[idx + 1]:
            return False

    return True


def _fill_element_in_print_strings(height, idx, array, curr_row, curr_col, print_strings):
    print_strings[curr_row][curr_col] = str(array[idx])

    left_child = 2 * idx + 1
    right_child = 2 * idx + 2

    if left_child < len(array):
        _fill_element_in_print_strings(height, left_child, array, curr_row + 1, curr_col - 2**(height - curr_row - 1), print_strings)
    if right_child < len(array):
        _fill_element_in_print_strings(height, right_child, array, curr_row + 1, curr_col + 2**(height - curr_row - 1), print_strings)

    return


def get_array_print_string_as_complete_binary_tree(array):
    n = len(array)
    h = int(math.log2(n)) + 1

    num_rows = h
    num_cols = (2 ** num_rows) - 1

    print_strings = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    _fill_element_in_print_strings(h - 1, 0, array, 0, int((num_cols - 1) / 2), print_strings)

    return '\n'.join(['\t'.join(each_row) for each_row in print_strings])


if __name__ == "__main__":
    # n = 10
    # mat = list()
    # for _ in range(n):
    #     curr_list = list()
    #     for _ in range(n):
    #         curr_list.append(random.randint(0, 1))
    #     mat.append(curr_list)

    # print_2d_matrix(mat, None, ' | ', True, False)
    items = list(range(15))
    print(get_array_print_string_as_complete_binary_tree(items))

