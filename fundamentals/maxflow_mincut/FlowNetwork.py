from FlowEdge import FlowEdge


class FlowNetwork:
    def __init__(self, num_vertices):
        self.adj = [[] for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        return

    def add_edge(self, flow_edge):
        v = flow_edge.from_vertex()
        w = flow_edge.to_vertex()

        self.adj[v].append(flow_edge)
        self.adj[w].append(flow_edge)
        return

    def adjacent(self, vertex):
        return self.adj[vertex]

    def number_of_vertices(self):
        return self.num_vertices
