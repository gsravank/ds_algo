from fundamentals.directed_graphs.DiGraph import DiGraph
import random
import matplotlib.pyplot as plt


class DirectedDFS:
    def __init__(self, digraph, start_vertices):
        self.visited = [False for _ in range(digraph.num_vertices())]

        for vertex in start_vertices:
            if not self.marked(vertex):
                self._dfs(vertex, digraph)

        return

    def _dfs(self, vertex, digraph):
        self.visited[vertex] = True
        for neighbor in digraph.adjacent(vertex):
            if not self.marked(neighbor):
                self._dfs(neighbor, digraph)
        return

    def marked(self, v):
        return self.visited[v]


if __name__ == "__main__":
    num_vertices = 20
    graph = DiGraph(num_vertices)
    edges = []
    all_vertices = list(range(num_vertices))
    for _ in range(10):
        v = random.sample(all_vertices, 1)[0]
        w = random.sample([x for x in all_vertices if x != v], 1)[0]
        edges.append((v, w))
    edges = list(set(edges))
    for v, w in edges:
        graph.add_edge(v, w)

    print(graph)

    start_vertices = random.sample(all_vertices, 2)
    dfs = DirectedDFS(graph, start_vertices)
    print('\n')
    print('Start: ' + " ".join([str(x) for x in start_vertices]))
    reachable = [v for v in all_vertices if dfs.marked(v)]
    print('Reachable: ' + " ".join([str(x) for x in reachable]))

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    graph.plot(ax, 'o', 'b', 'k')
    plt.show()
