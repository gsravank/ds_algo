import math
from utils.PlotUtils import plot_line_ax

from Point2D import Point2D


class RectHV:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.corners = [Point2D(x_min, y_min), Point2D(x_min, y_max), Point2D(x_max, y_min), Point2D(x_max, y_max)]

    def x_min(self):
        return self.x_min

    def x_max(self):
        return self.x_max

    def y_min(self):
        return self.y_min

    def y_max(self):
        return self.y_max

    def contains(self, point):
        return (self.x_min <= point.x <= self.x_max) and (self.y_min <= point.y <= self.y_max)

    def intersects(self, other):
        for corner in self.corners:
            if other.contains(corner):
                return True
        return False

    def distance_squared_to(self, point):
        return self.distance_to(point) ** 2

    def distance_to(self, point):
        if self.x_min <= point.x <= self.x_max:
            if self.y_min <= point.y <= self.y_max:
                return 0
            else:
                return min(math.fabs(point.y - self.y_min), math.fabs(point.y - self.y_max))
        elif self.y_min <= point.y <= self.y_max:
            return min(math.fabs(point.x - self.x_min), math.fabs(point.x - self.x_max))
        else:
            return min([point.distance_to(corner) for corner in self.corners])

    def __eq__(self, other):
        return self.x_min == other.x_min and self.x_max == other.x_max \
               and self.y_min == other.y_min and self.y_max == other.y_max

    def __str__(self):
        return f"[{self.x_min}, {self.x_max}] x [{self.y_min}, {self.y_max}]"

    def __hash__(self):
        return hash(self.__str__())

    def plot(self, ax, marker='o', color='b', plot_corners=True):
        if plot_corners:
            for corner in self.corners:
                corner.plot(ax, marker, color)

        _ = plot_line_ax(ax, self.x_min, self.y_min, self.x_max, self.y_min, color)
        _ = plot_line_ax(ax, self.x_min, self.y_min, self.x_min, self.y_max, color)
        _ = plot_line_ax(ax, self.x_min, self.y_max, self.x_max, self.y_max, color)
        _ = plot_line_ax(ax, self.x_max, self.y_max, self.x_max, self.y_min, color)

        return
