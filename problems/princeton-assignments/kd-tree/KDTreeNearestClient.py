import random
from utils.PlotUtils import plot_point_ax
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
        pset.insert(point)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    pset.plot(ax)
    plt.show()

    while True:
        inp = input()
        items = [float(x.strip()) for x in inp.strip().split(' ') if len(x.strip())]
        query_point = Point2D(items[0], items[1])
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        pset.plot(ax)
        nearest = pset.nearest(query_point, ax)
        plot_point_ax(ax, query_point.x, query_point.y, 'x', 'g')
        plot_point_ax(ax, nearest.x, nearest.y, 'x', 'r')
        plt.show()
    return


if __name__ == "__main__":
    fn = 'data/circle1000.txt'
    main(fn)
