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
    times = list()
    items = list(range(10000))
    for _ in tqdm(range(1000)):
        t1 = time.time()
        QuickSortThreeWay.sort(items)
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

    return


if __name__ == "__main__":
    main()
