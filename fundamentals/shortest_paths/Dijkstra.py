from WeightedDiEdge import WeightedDiEdge
from IndexedMinPQ import IndexedMinPQ
import math
from EdgeWeightedDiGraph import EdgeWeightedDiGraph


class DijkstraSP:
    def __init__(self, ewdgraph, source):
        self.graph = ewdgraph
        self.num_vertices = ewdgraph.num_vertices()

        # Data Structures
        self.dist_to = [math.inf for _ in range(self.num_vertices)]
        self.dist_to[source] = 0

        self.edge_to = [None for _ in range(self.num_vertices)]

        self.indexed_pq = IndexedMinPQ(self.num_vertices)

        # Process
        self.indexed_pq.insert(source, 0)
        while not self.indexed_pq.is_empty():
            # Pick closest vertex to the source
            closest_vertex = self.indexed_pq.delete_min()

            # Relax all outgoing edges from this vertex
            outgoing_edges = ewdgraph.adjacent(closest_vertex)
            for edge in outgoing_edges:
                self.relax(edge)

        return

    def relax(self, edge):
        v = edge.from_vertex()
        w = edge.to_vertex()
        
        if self.dist_to[w] > self.dist_to[v] + edge.weight():
            self.dist_to[w] = self.dist_to[v] + edge.weight()
            self.edge_to[w] = edge
            
            if self.indexed_pq.contains(w):
                self.indexed_pq.decrease_key(w, self.dist_to[w])
            else:
                self.indexed_pq.insert(w, self.dist_to[w])
        
        return

    def distance_to(self, v):
        return self.dist_to[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        curr_vertex = v
        path = list()
        while curr_vertex is not None:
            path.append(curr_vertex)
            curr_vertex = self.edge_to[curr_vertex]

        return path

    def has_path_to(self, v):
        return self.distance_to(v) != math.inf


if __name__ == '__main__':
    graph = EdgeWeightedDiGraph(8)
    edges = [(0, 1, 5), (0, 4, 9), (0, 7, 8), (1, 7, 4), (1, 3, 15), (1, 2, 12),
             (2, 3, 3), (2, 6, 11), (3, 6, 9), (4, 7, 5), (4, 5, 4), (4, 6, 20),
             (5, 2, 1), (5, 6, 13), (7, 5, 6), (7, 2, 7)]
    for v, w, weight in edges:
        graph.add_edge(WeightedDiEdge(v, w, weight))

    print(graph)

    dij_sp = DijkstraSP(graph, 0)
    print(dij_sp.dist_to)
    print(dij_sp.edge_to)

