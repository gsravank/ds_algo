from DiGraph import DiGraph
import matplotlib.pyplot as plt
import random


class TopoSort:
    def __init__(self, graph):
        self.visited = [False for _ in range(graph.num_vertices())]
        self.topo_order = list()

        for v in range(graph.num_vertices()):
            if not self.visited[v]:
                self.dfs(graph, v)

        self.topo_order = self.topo_order[::-1]
        return

    def dfs(self, graph, v):
        self.visited[v] = True

        for w in graph.adjacent(v):
            if not self.visited[w]:
                self.dfs(graph, w)

        self.topo_order.append(v)
        return

    def topological_order(self):
        return self.topo_order


if __name__ == "__main__":
    edges = [(0, 5), (0, 1), (3, 5), (5, 2), (6, 0), (1, 4), (0, 2), (3, 6), (3, 4), (6, 4), (3, 2)]
    graph = DiGraph(7)
    for v, w in edges:
        graph.add_edge(v, w)

    print(graph)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()

    ts = TopoSort(graph)
    topological_order = ts.topological_order()
    print(topological_order)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()
