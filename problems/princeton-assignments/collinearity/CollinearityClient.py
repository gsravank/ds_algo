from BruteForceCollinearity import BruteForce
from FasterCollinearity import FastCollinearity
from Point import Point
import matplotlib.pyplot as plt
from utils.PlotUtils import plot_point_ax, plot_line_ax


def get_points_from_file(filename):
    idx = 0
    points = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            if idx == 0:
                pass
            else:
                line = line.strip()
                items = [x for x in line.split(' ') if len(x.strip())]
                if len(items):
                    points.append(Point(int(items[0]), int(items[1])))

    return points


def main(filename):
    points = get_points_from_file(filename)
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    for point in points:
        plot_point_ax(ax, point.x, point.y, 'o', 'b')
    _ = plt.show()

    # coll_obj = BruteForce(points)
    coll_obj = FastCollinearity(points)
    print(coll_obj.number_of_segments())
    for x in coll_obj.segments():
        print(x)

    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    for point in points:
        plot_point_ax(ax, point.x, point.y, 'o', 'b')

    for seg in coll_obj.segments():
        p1, p2 = seg.p, seg.q
        plot_line_ax(ax, p1.x, p1.y, p2.x, p2.y, 'k')

    _ = plt.show()
    return


if __name__ == "__main__":
    fn = '/Users/sravan/Downloads/collinear/rs1423.txt'
    main(fn)