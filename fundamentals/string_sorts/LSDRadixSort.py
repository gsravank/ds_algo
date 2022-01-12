import string
import random
from KeyIndexedCounting import KeyIndexedCounting


class LSDRadixSort:
    def __init__(self, sorted_keys=None):
        self.kic = KeyIndexedCounting(sorted_keys)
        return

    def sort(self, array):
        if not len(array):
            return

        D = len(array[0])
        for d in range(D-1, -1, -1):
            self.kic.sort(array, d)
            # print('\n'.join(array))
            # print('\n--\n')
        return


if __name__ == '__main__':
    obj = LSDRadixSort(string.ascii_lowercase)

    arr = list()
    str_len = 5
    # population = random.sample(string.ascii_lowercase, 5)
    population = string.ascii_lowercase[:5]
    # print(sorted(population))
    for _ in range(10):
        arr.append(''.join(random.choices(population, k=str_len)))

    print('\n'.join(arr) + '\n========\n')
    obj.sort(arr)
    print('\n'.join(arr) + '\n========\n')


