import math
from utils.PlotUtils import plot_point_ax, plot_line_ax


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    def distance_squared_to(self, other):
        return (other.y - self.y)**2 + (other.x - self.x)**2

    def distance_to(self, other):
        return math.sqrt(self.distance_squared_to(other))

    def compare_to(self, other):
        return self.x - other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.__str__())

    def plot(self, ax, marker='o', color='b'):
        _ = plot_point_ax(ax, self.x, self.y, marker, color)
        return
