from Point2D import Point2D
from RectHV import RectHV
import matplotlib.pyplot as plt


class PointSET:
    def __init__(self):
        self.points = set([])
        return

    def is_empty(self):
        return len(self.points) == 0

    def size(self):
        return len(self.points)

    def insert(self, point):
        self.points = self.points.union([point])
        return

    def contains(self, point):
        return point in self.points

    def plot(self, ax, marker='o', color='b'):
        for point in self.points:
            _ = point.plot(ax, marker, color)
        return

    def range(self, rect, ax=None):
        range_points = list()
        for point in self.points:
            if rect.contains(point):
                range_points.append(point)

        if ax is not None:
            self.plot(ax)
            rect.plot(ax, plot_corners=False)

        return range_points

    def nearest(self, point):
        final = None
        smallest_distance = None

        for internal_point in self.points:
            curr_distance = internal_point.distance_to(point)
            if smallest_distance is None or curr_distance < smallest_distance:
                final = internal_point
                smallest_distance = curr_distance

        return final


def main(filename):
    points = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line.strip()):
                items = [float(x) for x in line.strip().split(' ') if len(x)]
                points.append(Point2D(items[0], items[1]))

    pset = PointSET()
    for point in points:
        # print(point)
        pset.insert(point)

    print(pset.size())
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    pset.plot(ax)
    plt.show()

    while True:
        items = input()
        xmin, xmax, ymin, ymax = [float(x) for x in items.strip().split(' ') if len(x)]
        user_rect = RectHV(xmin, xmax, ymin, ymax)
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        points_inside_rect = pset.range(user_rect, ax)
        for point in points_inside_rect:
            point.plot(ax, 'x', 'r')
        _ = plt.show()
        _ = plt.waitforbuttonpress(0)
        _ = plt.close(fig)


    return


if __name__ == "__main__":
    fn = '/Users/sravan/Downloads/kdtree/input10.txt'
    main(fn)
