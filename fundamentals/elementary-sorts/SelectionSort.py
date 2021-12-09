import random
import os

from utils.DSUtils import is_sorted
from classes.Date import Date


class SelectionSort:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        for index in range(len(array)):
            min_index = index
            for jdx in range(index, len(array)):
                if SelectionSort.less(array[jdx], array[min_index]):
                    min_index = jdx
            SelectionSort.swap(array, index, min_index)

            print(' '.join([str(x) for x in array]))

        return

    @staticmethod
    def less(first, second):
        return first < second

    @staticmethod
    def swap(array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    # items = random.sample(list(range(100)), 70)
    items = random.sample(list(range(1, 31)), 30)
    # print(' '.join([str(x) for x in items]))
    # print('\n')
    # SelectionSort.sort(items)
    # print('\n')
    # print(' '.join([str(x) for x in items]))
    #
    # print(is_sorted(items))

    years = list(range(2000, 2021))
    months = list(range(1, 13))
    dates = list(range(1, 32))

    # items = list()
    # for _ in range(10):
    #     items.append(Date(random.sample(years, 1)[0], random.sample(months, 1)[0], random.sample(dates, 1)[0]))

    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))
    print('\n')
    SelectionSort.sort(items)
    print('\n')
    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))



