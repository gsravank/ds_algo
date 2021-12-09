from WeightedEdge import WeightedEdge


class EdgeWeightedGraph:
    def __init__(self, num_vertices):
        self.number_of_vertices = num_vertices
        self.number_of_edges = 0
        self.adj = [[] for _ in range(num_vertices)]
        return

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)

        self.adj[v].append(edge)
        self.adj[w].append(edge)

        self.number_of_edges += 1
        return

    def adjacent(self, v):
        return self.adj[v]

    def edges(self):
        return set([x for y in self.adj for x in y])

    def num_vertices(self):
        return self.number_of_vertices

    def num_edges(self):
        return self.number_of_edges

    def __repr__(self):
        strings = [f"{edge}" for edge in self.edges()]
        return "\n".join(strings)


if __name__ == '__main__':
    n = 5
    edges = [(0, 1, 1), (1, 3, 10), (2, 4, 3), (1, 4, 6)]
    graph = EdgeWeightedGraph(n)
    for v, w, weight in edges:
        graph.add_edge(WeightedEdge(v, w, weight))

    print(graph)
