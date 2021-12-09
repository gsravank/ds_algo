from EdgeWeightedDiGraph import EdgeWeightedDiGraph
import random
import matplotlib.pyplot as plt
from WeightedDiEdge import WeightedDiEdge
from TopoSortEWDiGraph import TopoSortEWDiGraph
import math


class EdgeWeightedDAGSP:
    def __init__(self, graph, source):
        self.graph = graph
        self.num_vertices = graph.num_vertices()
        self.dist_to = [math.inf for _ in range(self.num_vertices)]
        self.dist_to[source] = 0
        self.edge_to = [None for _ in range(self.num_vertices)]

        topo_order = TopoSortEWDiGraph(graph).topological_order()

        for vertex in topo_order:
            for edge in graph.adjacent(vertex):
                self.relax(edge)

        return

    def relax(self, edge):
        v = edge.from_vertex()
        w = edge.to_vertex()

        self.dist_to[w] = min(self.dist_to[w], self.dist_to[v] + edge.weight())
        self.edge_to[w] = edge
        return

    def distance_to(self, v):
        return self.dist_to[v]

    def path_to(self, v):
        if self.dist_to[v] == math.inf:
            return None

        path = list()
        curr_vertex = v
        while curr_vertex is not None:
            path.append(curr_vertex)
            curr_vertex = self.edge_to[curr_vertex].from_vertex()

        return path


if __name__ == '__main__':
    random.seed(0)
    edges = [(0, 5), (0, 1), (3, 5), (5, 2), (6, 0), (1, 4), (0, 2), (3, 6), (3, 4), (6, 4), (3, 2)]
    graph = EdgeWeightedDiGraph(7)
    for v, w in edges:
        graph.add_edge(WeightedDiEdge(v, w, random.randint(1, 20)))

    print(graph)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()

    sp = EdgeWeightedDAGSP(graph, 0)
    print(sp.dist_to)
    print(sp.edge_to)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()
