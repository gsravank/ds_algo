from WeightedDiEdge import WeightedDiEdge
import matplotlib.pyplot as plt
import math
from utils.PlotUtils import plot_point_ax, plot_line_ax, plot_text_ax
from matplotlib.patches import FancyArrowPatch


class EdgeWeightedDiGraph:
    def __init__(self, num_vertices):
        self.number_of_vertices = num_vertices
        self.number_of_edges = 0
        self.vertex_point_map = None
        self.adj = [[] for _ in range(num_vertices)]
        return

    def add_edge(self, edge):
        v = edge.from_vertex()
        self.adj[v].append(edge)
        self.number_of_edges += 1
        return

    def adjacent(self, v):
        return self.adj[v]

    def edges(self):
        return [x for y in self.adj for x in y]

    def num_vertices(self):
        return self.number_of_vertices

    def num_edges(self):
        return self.number_of_edges

    def __repr__(self):
        strings = [f"{edge}" for edge in self.edges()]
        return "\n".join(strings)

    def _get_circle_points(self, center, radius, num_points):
        points = list()
        for idx in range(num_points):
            angle = 2.0 * math.pi * idx / num_points
            x = center[0] + (radius * math.cos(angle))
            y = center[1] + (radius * math.sin(angle))
            points.append((x, y))
        return points

    def _generate_vertex_point_map(self):
        if self.vertex_point_map is not None:
            return

        vertex_point_map = dict()
        sorted_vertices = sorted(list(range(self.number_of_vertices)), key=lambda v: len(self.adj[v]))
        points = self._get_circle_points([0.5, 0.5], 0.4, self.number_of_vertices)

        vertex_point_map = dict(zip(sorted_vertices, points))

        self.vertex_point_map = vertex_point_map
        return

    def plot(self, ax, marker='o', vcolor='b', ecolor='b', vertex_point_map=None):
        if vertex_point_map is None:
            self._generate_vertex_point_map()

        for v in range(self.number_of_vertices):
            plot_point_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1], marker, vcolor)
            plot_text_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1] + 0.02, str(v))
            for edge in self.adj[v]:
                w = edge.to_vertex()
                plot_line_ax(ax, self.vertex_point_map[v][0], self.vertex_point_map[v][1], self.vertex_point_map[w][0],
                             self.vertex_point_map[w][1], ecolor)
                ar = FancyArrowPatch((self.vertex_point_map[v][0], self.vertex_point_map[v][1]),
                                     (self.vertex_point_map[w][0], self.vertex_point_map[w][1]),
                                     arrowstyle='->', mutation_scale=20)
                ax.add_patch(ar)

                mid_point = (self.vertex_point_map[v][0] + self.vertex_point_map[w][0]) / 2.0, \
                            (self.vertex_point_map[v][1] + self.vertex_point_map[w][1]) / 2.0
                plot_text_ax(ax, mid_point[0], mid_point[1], edge.weight())

        return


if __name__ == '__main__':
    n = 5
    edges = [(0, 1, 1), (1, 3, 10), (2, 4, 3), (1, 4, 6)]
    graph = EdgeWeightedDiGraph(n)
    for v, w, weight in edges:
        graph.add_edge(WeightedDiEdge(v, w, weight))

    print(graph)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()
