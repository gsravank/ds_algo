import math
import os
from RectHV import RectHV
import random
from Point2D import Point2D
from utils.PlotUtils import plot_point_ax, plot_line_ax


class Node:
    def __init__(self, point):
        self.key = point
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}"


class KDTree:
    def __init__(self):
        self.root = None
        self.size_ = 0

    def size(self):
        return self.size_

    @staticmethod
    def _search(node, point, level):
        if node is None:
            return None

        if level % 2 == 0:
            # Check x-coordinate
            if node.key.x > point.x:
                return KDTree._search(node.left, point, level + 1)
            elif node.key.x == point.x and node.key.y == point.y:
                return node
            else:
                return KDTree._search(node.right, point, level + 1)
        else:
            # Check y-coordinate
            if node.key.y > point.y:
                return KDTree._search(node.left, point, level + 1)
            elif node.key.x == point.x and node.key.y == point.y:
                return node
            else:
                return KDTree._search(node.right, point, level + 1)

    def search(self, point):
        return KDTree._search(self.root, point, 0)

    @staticmethod
    def _insert(node, point, level):
        if node is None:
            return Node(point)

        if level % 2 == 0:
            # Check x-coordinate
            if node.key.x > point.x:
                node.left = KDTree._insert(node.left, point, level + 1)
            elif node.key.x == point.x and node.key.y == point.y:
                pass
            else:
                node.right = KDTree._insert(node.right, point, level + 1)
        else:
            # Check y-coordinate
            if node.key.y > point.y:
                node.left = KDTree._insert(node.left, point, level + 1)
            elif node.key.x == point.x and node.key.y == point.y:
                pass
            else:
                node.right = KDTree._insert(node.right, point, level + 1)

        return node

    def insert(self, point):
        self.root = KDTree._insert(self.root, point, 0)
        self.size_ += 1
        return

    @staticmethod
    def _plot(node, ax, hv_flag, x_min, x_max, y_min, y_max):
        if node is None:
            return

        plot_point_ax(ax, node.key.x, node.key.y, marker='o', color='k')
        if hv_flag == 0:
            plot_line_ax(ax, x_min, node.key.y, x_max, node.key.y, color='b')
            KDTree._plot(node.left, ax, 1 - hv_flag, x_min, x_max, y_min, node.key.y)
            KDTree._plot(node.right, ax, 1 - hv_flag, x_min, x_max, node.key.y, y_max)
        else:
            plot_line_ax(ax, node.key.x, y_min, node.key.x, y_max, color='r')
            KDTree._plot(node.left, ax, 1 - hv_flag, x_min, node.key.x, y_min, y_max)
            KDTree._plot(node.right, ax, 1 - hv_flag, node.key.x, x_max, y_min, y_max)

        return

    def plot(self, ax):
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        KDTree._plot(self.root, ax, 1, 0, 1, 0, 1)
        return

    @staticmethod
    def _range(node, query_rect, x_min, x_max, y_min, y_max, level, point_list):
        if node is None:
            return

        node_rect = RectHV(x_min, x_max, y_min, y_max)
        if node_rect.intersects(query_rect):
            point_list.append(node.key)

            if level % 2 == 0:
                KDTree._range(node.left, query_rect, x_min, node.key.x, y_min, y_max, level + 1, point_list)
                KDTree._range(node.right, query_rect, node.key.x, x_max, y_min, y_max, level + 1, point_list)
            else:
                KDTree._range(node.left, query_rect, x_min, x_max, y_min, node.key.y, level + 1, point_list)
                KDTree._range(node.right, query_rect, x_min, x_max, node.key.y, y_max, level + 1, point_list)
        return

    def range(self, query_rect, ax=None):
        final_list = list()
        KDTree._range(self.root, query_rect, 0, 1, 0, 1, 0, final_list)

        if ax is not None:
            self.plot(ax)
            query_rect.plot(ax, plot_corners=False, color='k')

        return final_list

    @staticmethod
    def _nearest(node, point, x_min, x_max, y_min, y_max, level, min_distance, min_point, ax=None):
        if node is None:
            print(min_point, min_distance, None)
            return min_distance, min_point
        print(min_point, min_distance, node.key)
        if ax is not None:
            plot_point_ax(ax, node.key.x, node.key.y, 'x', 'r')

        curr_distance = point.distance_to(node.key)
        curr_point = node.key
        if curr_distance < min_distance:
            min_point = curr_point
            min_distance = curr_distance

        if level % 2 == 0:
            left_rect = RectHV(x_min, node.key.x, y_min, y_max)
            right_rect = RectHV(node.key.x, x_max, y_min, y_max)
            if left_rect.distance_to(point) <= min_distance:
                min_distance, min_point = KDTree._nearest(node.left, point, x_min, node.key.x, y_min, y_max,
                                                          level + 1, min_distance, min_point, ax)
            if right_rect.distance_to(point) <= min_distance:
                min_distance, min_point = KDTree._nearest(node.right, point, node.key.x, x_max, y_min, y_max,
                                                          level + 1, min_distance, min_point, ax)
        else:
            left_rect = RectHV(x_min, x_max, y_min, node.key.y)
            right_rect = RectHV(x_min, x_max, node.key.y, y_max)
            if left_rect.distance_to(point) <= min_distance:
                min_distance, min_point = KDTree._nearest(node.left, point, x_min, x_max, y_min, node.key.y,
                                                          level + 1, min_distance, min_point, ax)
            if right_rect.distance_to(point) <= min_distance:
                min_distance, min_point = KDTree._nearest(node.right, point, x_min, x_max, node.key.y, y_max,
                                                          level + 1, min_distance, min_point, ax)

        return min_distance, min_point

    def nearest(self, point, ax=None):
        closest_distance, closest_point = KDTree._nearest(self.root, point, 0, 1, 0, 1, 0, math.inf, None, ax)
        return closest_point
