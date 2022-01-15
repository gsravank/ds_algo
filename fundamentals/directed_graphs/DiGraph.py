import math
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import random
from utils.PlotUtils import plot_point_ax, plot_line_ax, plot_text_ax


class DiGraph:
    def __init__(self, num_of_vertices):
        self.number_of_vertices = num_of_vertices
        self.number_of_edges = 0
        self.vertex_point_map = None

        self.adjacency_list = [[] for _ in range(num_of_vertices)]

    def add_edge(self, v, w):
        assert v < self.number_of_vertices and w < self.number_of_vertices
        self.adjacency_list[v].append(w)
        # self.adjacency_list[w].append(v)
        self.number_of_edges += 1
        return

    def adjacent(self, v):
        return self.adjacency_list[v]

    def num_vertices(self):
        return self.number_of_vertices

    def num_edges(self):
        return self.number_of_edges

    def reverse(self):
        rev_graph = DiGraph(self.num_vertices())
        for v in range(self.num_vertices()):
            for w in self.adjacent(v):
                rev_graph.add_edge(w, v)
        return rev_graph

    def __repr__(self):
        strings = list()
        for v in range(self.number_of_vertices):
            for w in self.adjacency_list[v]:
                strings.append(f"{v}-{w}")
        return '\n'.join(strings)

    @staticmethod
    def _get_circle_points(center, radius, num_points, start_angle=0):
        points = list()
        for idx in range(num_points):
            angle = start_angle + (2.0 * math.pi * idx / num_points)
            x = center[0] + (radius * math.cos(angle))
            y = center[1] + (radius * math.sin(angle))
            points.append((x, y))
        return points

    def _generate_vertex_point_map(self):
        if self.vertex_point_map is not None:
            return

        vertex_point_map = dict()
        sorted_vertices = sorted(list(range(self.number_of_vertices)), key=lambda v: len(self.adjacency_list[v]))
        sorted_vertices = list(range(self.number_of_vertices))
        points = self._get_circle_points([0.5, 0.5], 0.4, self.number_of_vertices)

        vertex_point_map = dict(zip(sorted_vertices, points))

        self.vertex_point_map = vertex_point_map
        return

    def plot(self, ax, marker='o', vcolor='b', ecolor='b', vertex_point_map=None, texts=None):
        if vertex_point_map is None:
            self._generate_vertex_point_map()
        else:
            self.vertex_point_map = vertex_point_map
        if texts is None:
            texts = list(range(self.number_of_vertices))

        for v in range(self.number_of_vertices):
            plot_point_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1], marker, vcolor)
            plot_text_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1] + 0.02, str(texts[v]))
            for w in self.adjacency_list[v]:
                plot_line_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1], self.vertex_point_map[w][0],
                             self.vertex_point_map[w][1], ecolor)
                ar = FancyArrowPatch((self.vertex_point_map[v][0], self.vertex_point_map[v][1]),
                                     (self.vertex_point_map[w][0], self.vertex_point_map[w][1]),
                                     arrowstyle='->', mutation_scale=20)
                ax.add_patch(ar)

        return

    def plot_edge(self, ax, v, w, color='k'):
        self._generate_vertex_point_map()
        plot_line_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1],
                     self.vertex_point_map[w][0], self.vertex_point_map[w][1], color)
        return

    def plot_edges(self, ax, edges, color='k'):
        for edge in edges:
            self.plot_edge(ax, edge[0], edge[1], color)
        return


if __name__ == "__main__":
    num_vertices = 10
    graph = DiGraph(num_vertices)
    edges = []
    all_vertices = list(range(num_vertices))
    for _ in range(20):
        v = random.sample(all_vertices, 1)[0]
        w = random.sample([x for x in all_vertices if x != v], 1)[0]
        edges.append((v, w))
    edges = list(set(edges))
    for v, w in edges:
        graph.add_edge(v, w)

    print(graph)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()