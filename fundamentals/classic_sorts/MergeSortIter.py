import os
import random
from utils.DSUtils import is_sorted
from classes.Date import Date


class MergeSortIter:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        aux = array[:]

        size = 1
        N = len(array)
        while size < N:
            for low in range(0, N - size, 2 * size):
                MergeSortIter._merge(array, aux, low, low + size - 1, min(low + size - 1 + size, N - 1))

            size *= 2
            # print('\n')
            # print(array)
            # print('\n')

        return

    @staticmethod
    def _merge(array, aux, low, mid, high):
        # print(low, mid,  high)
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
    # random.seed(1)
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
    MergeSortIter.sort(items)
    print('\n')
    print(' '.join([str(x) for x in items]))
    print(is_sorted(items))
