"""
Kosaraju-Sharir Algorithm
"""
from DiGraph import DiGraph
from TopoSort import TopoSort
import matplotlib.pyplot as plt
import random


class StrongComponents:
    def __init__(self, graph):
        self.graph = graph
        self.id = [None for _ in range(graph.num_vertices())]
        self.visited = [False for _ in range(graph.num_vertices())]
        self.count = 0

        dfs_order = TopoSort(self.graph.reverse()).topological_order()
        print(dfs_order)

        for v in dfs_order:
            if not self.visited[v]:
                self.dfs(v)
                self.count += 1

        print(self.id)
        return

    def dfs(self, v):
        self.visited[v] = True
        self.id[v] = self.count

        for w in self.graph.adjacent(v):
            if not self.visited[w]:
                self.dfs(w)
        return

    def strongly_connected(self, v, w):
        return self.id[v] == self.id[w]

    def get_id(self, v):
        return self.id[v]

    def get_count(self):
        return self.count


if __name__ == "__main__":
    graph = DiGraph(13)
    edges = [(0, 1), (0, 5), (2, 0), (2, 3), (3, 2), (3, 5), (4, 3), (4, 2),
             (5, 4), (6, 0), (6, 4), (6, 8), (6, 9), (7, 6), (7, 9), (8, 6),
             (9, 10), (9, 11), (10, 12), (11, 4), (11, 12), (12, 9)]
    for v, w in edges:
        graph.add_edge(v, w)

    print(graph)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()

    scc = StrongComponents(graph)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()
