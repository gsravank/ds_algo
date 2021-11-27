import os
import matplotlib.pyplot as plt
import random
from Graph import Graph


class CC:
    def __init__(self, graph, plot=False):
        self.graph = graph

        self.visited = [False for _ in range(self.graph.num_vertices())]
        self._id = [None for _ in range(self.graph.num_vertices())]
        self._count = 0
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        for vertex in range(self.graph.num_vertices()):
            if not self.visited[vertex]:
                self._cc(vertex, plot)

                if plot:
                    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
                    self.graph.plot(ax, 'o', 'k', 'k')
                    for v in range(self.graph.num_vertices()):
                        if self.visited[v]:
                            for w in self.graph.adjacent(v):
                                self.graph.plot_edge(ax, v, w, self.colors[self._id[v] % len(self.colors)])
                    plt.show()

                self._count += 1

    def _cc(self, vertex, plot=False):
        self.visited[vertex] = True
        self._id[vertex] = self._count
        for neighbor in self.graph.adjacent(vertex):
            if not self.visited[neighbor]:
               self._cc(neighbor, plot)
        return

    def count(self):
        return self._count

    def id(self, v):
        return self._id[v]


if __name__ == "__main__":
    num_vertices = 20
    graph = Graph(num_vertices)
    edges = []
    all_vertices = list(range(num_vertices))
    for _ in range(15):
        v = random.sample(all_vertices, 1)[0]
        w = random.sample([x for x in all_vertices if x != v], 1)[0]
        edges.append((v, w))
    edges = list(set(edges))
    for v, w in edges:
        graph.add_edge(v, w)

    # print(graph)
    # fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    # graph.plot(ax, 'o', 'b', 'k')
    # plt.show(block=False)

    cc = CC(graph, True)

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    graph.plot(ax, 'o', 'k', 'k')
    for v in range(graph.num_vertices()):
        if cc.visited[v]:
            for w in graph.adjacent(v):
                graph.plot_edge(ax, v, w, cc.colors[cc.id(v) % len(cc.colors)])
    plt.show(block=False)
    print("Done")

    while True:
        inp = input()
        items = [x.strip() for x in inp.strip().split(' ') if len(x.strip())]

        if len(items) == 2:
            print(f"Are {items[0]} and {items[1]} connected? {cc.id(int(items[0])) == cc.id(int(items[1]))}")
        elif len(items) == 1:
            print(f"ID of {items[0]}: {cc.id(int(items[0]))}")
