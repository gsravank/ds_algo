import random
import os
from utils.DSUtils import is_sorted, get_array_print_string


class ShellSort:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        # Get h to be used as increment via (3x + 1) method
        h = 1
        while h < int(len(array) / 3):
            h = 3 * h + 1

        # Start with big-h and progressively reduce h
        # At each h, perform h stride insertion sort
        while h >= 1:
            print(f"h = {h}")
            for idx in range(h, len(array)):
                for jdx in range(idx, h - 1, -h):
                    if ShellSort.less(array[jdx], array[jdx - h]):
                        ShellSort.swap(array, jdx, jdx - h)
                    else:
                        break
                if idx < len(array):
                    print(get_array_print_string(array, [idx], True))

            h = int(h / 3)

        return

    @staticmethod
    def less(first, second):
        return first < second

    @staticmethod
    def swap(array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    random.seed(1)
    # items = random.sample(list(range(100)), 70)
    items = random.sample(list(range(1, 31)), 30)

    years = list(range(2000, 2021))
    months = list(range(1, 13))
    dates = list(range(1, 32))

    # items = list()
    # for _ in range(10):
    #     items.append(Date(random.sample(years, 1)[0], random.sample(months, 1)[0], random.sample(dates, 1)[0]))

    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))
    print('\n')
    ShellSort.sort(items)
    print('\n')
    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))
