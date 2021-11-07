import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import time

from utils.DSUtils import is_sorted
from MaxHeap import MaxHeap


class HeapSort:
    def __init__(self):
        return

    @staticmethod
    def sort(array):
        max_heap = MaxHeap(array)

        for _ in range(len(array)):
            max_elem = max_heap.delete_max()
            # array[-1] = max_elem
        return


if __name__ == "__main__":
    items = list(range(1000))

    # print(items)
    # HeapSort.sort(items)
    # print(items)
    # print(is_sorted(items))

    times = list()
    for _ in tqdm(range(1000)):
        random.shuffle(items)
        t1 = time.time()
        HeapSort.sort(items)
        t2 = time.time()
        if not is_sorted(items):
            print(items)
        times.append(t2 - t1)

    print(np.mean(times))
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.hist(times, 100)
    plt.show()
