import random, os
from QuickSort import QuickSort
from classes.Date import Date
from utils.DSUtils import is_sorted
from QuickSortThreeWay import QuickSortThreeWay
import time
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


def main():
    times_a = list()
    times_b = list()

    items = [random.randint(1, 5) for _ in range(1000)]
    items = [random.randint(1, 100) for _ in range(1000)]
    items = list(range(1000))
    for _ in tqdm(range(1000)):
        t1 = time.time()
        QuickSortThreeWay.sort(items)
        t2 = time.time()
        times_a.append(t2 - t1)
        if not is_sorted(items):
            print("ThreeWay Sort")
            print(items)

    for _ in tqdm(range(1000)):
        t1 = time.time()
        QuickSort.sort(items)
        t2 = time.time()
        times_b.append(t2 - t1)
        if not is_sorted(items):
            print("GenSort")
            print(items)

    # print('\n')
    # print(items)
    # print(is_sorted(items))

    print(np.mean(times_a))
    print(np.mean(times_b))
    print(np.mean(times_b) / np.mean(times_a))

    fig, ax = plt.subplots(1, 2, figsize=(20, 6))
    ax[0].hist(times_a, 100)
    ax[1].hist(times_b, 100)
    ax[0].set_title("ThreeWay Sort")
    ax[1].set_title("Gen Sort")
    plt.show()

    return


if __name__ == "__main__":
    main()
