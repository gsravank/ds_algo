import os
import random


class KnuthShuffle:
    def __init__(self):
        return

    @staticmethod
    def shuffle(array):
        for idx in range(len(array)):
            rand_idx = random.randint(0, idx)
            KnuthShuffle.swap(array, idx, rand_idx)

    @staticmethod
    def swap(array, i, j):
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    items = list(range(1, 11))
    print(items)

    KnuthShuffle.shuffle(items)
    print(items)