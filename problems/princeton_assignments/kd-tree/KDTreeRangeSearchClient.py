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

    # fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    # pset.plot(ax)
    # plt.show()

    # while True:
    #     items = input()
    #     xmin, xmax, ymin, ymax = [float(x) for x in items.strip().split(' ') if len(x)]
    #     user_rect = RectHV(xmin, xmax, ymin, ymax)
    #     fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    #     points_inside_rect = pset.range(user_rect, ax)
    #     for point in points_inside_rect:
    #         point.plot(ax, 'x', 'r')
    #     _ = plt.show()

    times = list()
    for _ in tqdm(range(1000)):
        two_rands = random.random(), random.random()
        x_min, x_max = min(two_rands), max(two_rands)
        two_rands = random.random(), random.random()
        y_min, y_max = min(two_rands), max(two_rands)

        query_rect = RectHV(x_min, x_max, y_min, y_max)

        t1 = time.time()
        _ = pset.range(query_rect)
        t2 = time.time()
        times.append(t2 - t1)

    df = pd.DataFrame({'times': times})
    print(df.describe([0.01, 0.05, 0.1, 0.2, 0.25, 0.5, 0.75, 0.8, 0.9, 0.95, 0.99]))

    return


if __name__ == "__main__":
    fn = 'data/input20K.txt'
    main(fn)
