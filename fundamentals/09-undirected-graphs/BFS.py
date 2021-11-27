import os
from collections import deque
import matplotlib.pyplot as plt
import random
from Graph import Graph


class BFS:
    def __init__(self, graph, start_vertex, plot=False):
        self.graph = graph
        self.start_vertex = start_vertex

        self.visited = [False for _ in range(self.graph.num_vertices())]
        self.edge_to = [None for _ in range(self.graph.num_vertices())]
        self.distance_to = [None for _ in range(self.graph.num_vertices())]

        self.queue = deque()

        self._bfs(start_vertex, plot)

    def _bfs(self, vertex, plot=False):
        self.queue.appendleft(vertex)
        self.visited[vertex] = True
        self.distance_to[vertex] = 0

        while len(self.queue):
            curr_vertex = self.queue.pop()
            self.visited[curr_vertex] = True
            neighbours = self.graph.adjacent(curr_vertex)

            for neighbour in neighbours:
                if not self.visited[neighbour]:
                    self.distance_to[neighbour] = 1 + self.distance_to[curr_vertex]
                    self.edge_to[neighbour] = curr_vertex
                    self.queue.appendleft(neighbour)
                    if plot:
                        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
                        self.graph.plot(ax, 'o', 'b', 'k')
                        plot_edges = list()
                        for idx in range(self.graph.num_vertices()):
                            _curr_vertex = idx
                            _parent = self.edge_to[_curr_vertex]
                            if _parent is not None:
                                plot_edges.append((_curr_vertex, _parent))
                        self.graph.plot_edges(ax, plot_edges, 'r')
                        plt.show()

        # print(self.visited)
        # print(self.queue)
        # print(self.distance_to)
        # print(self.edge_to)
        return

    def has_path_to(self, vertex):
        return self.visited[vertex]

    def path_to(self, vertex):
        if not self.has_path_to(vertex):
            return None

        path = list()
        curr_vertex = vertex
        while curr_vertex != self.start_vertex:
            path.append(curr_vertex)
            curr_vertex = self.edge_to[curr_vertex]

        path.append(self.start_vertex)
        return path


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

    bfs = BFS(graph, 0, True)

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    graph.plot(ax, 'o', 'b', 'k')
    plot_edges = list()
    for idx in range(graph.num_vertices()):
        curr_vertex = idx
        parent = bfs.edge_to[curr_vertex]
        if parent is not None:
            plot_edges.append((curr_vertex, parent))
    graph.plot_edges(ax, plot_edges, 'r')
    plt.show(block=False)
    print("Done")

    while True:
        inp_vertex = int(input())
        _ = os.system('clear')
        print(inp_vertex)
        if bfs.has_path_to(inp_vertex):
            print(' <- '.join([str(x) for x in bfs.path_to(inp_vertex)]))
