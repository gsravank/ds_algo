import random
import numpy as np
import matplotlib.pyplot as plt
import time
from utils.DSUtils import get_array_print_string, is_sorted
from tqdm import tqdm


class QuickSortThreeWay:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        # Shuffle the array
        random.shuffle(array)
        print('\n=======\n')
        print(array)
        print('\n=======\n')

        # Sort from start to end
        QuickSortThreeWay._sort(array, 0, len(array) - 1)
        return

    @staticmethod
    def _partition(array, low, high):
        left = low
        right = high
        i = low
        pivot_element = array[low]

        while i <= right:
            # print(get_array_print_string(array, [low, left, i, right], False))
            # print('\n')
            if array[i] == pivot_element:
                i += 1
            elif array[i] < pivot_element:
                QuickSortThreeWay._swap(array, left, i)
                left += 1
                i += 1
            else:
                QuickSortThreeWay._swap(array, i, right)
                right -= 1

        return left, right

    @staticmethod
    def _sort(array, low, high):
        if high <= low:
            return

        print(get_array_print_string(array, [low, high], False))
        left_pivot, right_pivot = QuickSortThreeWay._partition(array, low, high)
        print(get_array_print_string(array, [low, left_pivot, right_pivot, high], False))
        print('\n')
        QuickSortThreeWay._sort(array, low, left_pivot - 1)
        QuickSortThreeWay._sort(array, right_pivot + 1, high)

        return

    @staticmethod
    def _swap(array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    # items = [0 for _ in range(10)] + [1 for _ in range(10)] + [2 for _ in range(11)]
    items = list()
    for _ in range(32):
        curr = random.randint(1, 4)
        items.append(curr)
    random.shuffle(items)
    # items = [1] + items

    print(items)
    # n = len(items)
    # QuickSortThreeWay._partition(items, 0, n-1)
    # print('\n======\n')

    QuickSortThreeWay.sort(items)
    print('\n=========\n')
    print(items)
    print(is_sorted(items))
