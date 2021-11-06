import os
import random
from utils.DSUtils import is_sorted
from classes.Date import Date


class MergeSort:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        aux = array[:]
        MergeSort._sort(array, aux, 0, len(array) - 1)
        return

    @staticmethod
    def _sort(array, aux, low, high):
        if high <= low:
            return

        mid = low + int((high - low) / 2)
        MergeSort._sort(array, aux, low, mid)
        MergeSort._sort(array, aux, mid + 1, high)
        MergeSort._merge(array, aux, low, mid, high)
        return

    @staticmethod
    def _merge(array, aux, low, mid, high):
        for idx in range(low, high + 1):
            aux[idx] = array[idx]

        idx = low
        jdx = mid + 1

        for kdx in range(low, high + 1):
            if idx > mid:
                array[kdx] = aux[jdx]
                jdx += 1
            elif jdx > high:
                array[kdx] = aux[idx]
                idx += 1
            elif aux[jdx] <= aux[idx]:
                array[kdx] = aux[jdx]
                jdx += 1
            else:
                array[kdx] = aux[idx]
                idx += 1
        return


if __name__ == "__main__":
    random.seed(1)
    # items = random.sample(list(range(100)), 70)
    items = random.sample(list(range(1, 100)), 32)

    years = list(range(2000, 2021))
    months = list(range(1, 13))
    dates = list(range(1, 32))

    # items = list()
    # for _ in range(20):
    #     items.append(Date(random.sample(years, 1)[0], random.sample(months, 1)[0], random.sample(dates, 1)[0]))

    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))
    print('\n')
    MergeSort.sort(items)
    print('\n')
    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))
