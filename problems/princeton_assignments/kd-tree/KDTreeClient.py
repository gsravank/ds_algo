import random
import pandas as pd
import time
from tqdm import tqdm
from PointSET import PointSET
from KDTree import KDTree
from Point2D import Point2D
from RectHV import RectHV
import matplotlib.pyplot as plt


def main(filename):
    points = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line.strip()):
                items = [float(x) for x in line.strip().split(' ') if len(x)]
                points.append(Point2D(items[0], items[1]))

    # pset = PointSET()
    pset = KDTree()
    for point in points:
        # print(point)
        pset.insert(point)
        # fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        # pset.plot(ax)
        # plt.show(block=False)
        # plt.pause(1)
        # plt.close(fig)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    pset.plot(ax)
    plt.show()

    return


if __name__ == "__main__":
    fn = 'data/input10.txt'
    main(fn)
