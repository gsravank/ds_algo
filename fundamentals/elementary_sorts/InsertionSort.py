import random
import os

from utils.DSUtils import is_sorted, get_array_print_string
from classes.Date import Date


class InsertionSort:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        for idx in range(len(array)):
            for jdx in range(idx, 0, -1):
                if InsertionSort.less(array[jdx], array[jdx - 1]):
                    InsertionSort.swap(array, jdx, jdx - 1)
                else:
                    break
            if idx < len(array) - 1:
                print(get_array_print_string(array, [idx + 1]))
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
    InsertionSort.sort(items)
    print('\n')
    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))



