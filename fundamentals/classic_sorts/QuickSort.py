import random
import numpy as np
import matplotlib.pyplot as plt
import time
from utils.DSUtils import get_array_print_string, is_sorted
from tqdm import tqdm


class QuickSort:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        # Shuffle the array
        random.shuffle(array)
        # print('\n=======\n')
        # print(array)
        # print('\n=======\n')

        # Sort from start to end
        QuickSort._sort(array, 0, len(array) - 1)
        return

    @staticmethod
    def _partition(array, low, high):
        idx = low + 1
        jdx = high

        while True:
            # print('\n')
            # print(get_array_print_string(array, [idx, jdx], False))
            # Move idx to the right
            while array[idx] <= array[low]:
                idx += 1
                if idx >= high:
                    break

            # Move jdx to the left
            while array[jdx] > array[low]:
                jdx -= 1
                if jdx <= low:
                    break

            # Possibly swap idx and jdx
            if jdx > idx:
                QuickSort._swap(array, idx, jdx)
            else:
                break

        QuickSort._swap(array, low, jdx)

        return jdx

    @staticmethod
    def _sort(array, low, high):
        if high <= low:
            return

        # print(get_array_print_string(array, [low, high], False))
        pivot = QuickSort._partition(array, low, high)
        # print(get_array_print_string(array, [low, pivot, high], False))
        # print('\n')
        QuickSort._sort(array, low, pivot - 1)
        QuickSort._sort(array, pivot + 1, high)

        return

    @staticmethod
    def _swap(array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    items = list(range(32))
    # print(items)
    n = len(items)
    # QuickSort._partition(items, 0, n-1)

    times = list()
    items = list(range(10000))
    for _ in tqdm(range(1000)):
        t1 = time.time()
        QuickSort.sort(items)
        t2 = time.time()
        times.append(t2 - t1)
        if not is_sorted(items):
            print(items)
    # print('\n')
    # print(items)
    # print(is_sorted(items))

    print(np.mean(times))
    plt.hist(times, 100)
    plt.show()
