from EdgeWeightedGraph import EdgeWeightedGraph
import random
from WeightedEdge import WeightedEdge
from heapq import heappush, heappop, heapify


class PrimMST:
    def __init__(self, ewgraph):
        self.mst_weight = 0
        self.mst_edges = list()
        self.graph = ewgraph
        self.marked = [False for _ in range(ewgraph.num_vertices())]

        self.edge_pq = ewgraph.adjacent(0)
        heapify(self.edge_pq)
        self.marked[0] = True
        print(self.mst_edges)
        print(self.marked)
        print(self.edge_pq)
        print('\n')

        while len(self.edge_pq):
            best_edge = heappop(self.edge_pq)
            v = best_edge.either()
            w = best_edge.other(v)

            if self.marked[v] and self.marked[w]:
                continue

            if not self.marked[v]:
                self.visit(v)

            if not self.marked[w]:
                self.visit(w)

            self.mst_edges.append(best_edge)
            self.mst_weight += best_edge.weight()
            print(self.mst_edges)
            print(self.marked)
            print(self.edge_pq)
            print('\n')

        return

    def visit(self, v):
        self.marked[v] = True

        for edge in self.graph.adjacent(v):
            w = edge.other(v)

            if not self.marked[w]:
                heappush(self.edge_pq, edge)

        return

    def edges(self):
        return self.mst_edges

    def weight(self):
        return self.mst_weight


if __name__ == '__main__':
    graph = EdgeWeightedGraph(8)
    edges = [(0, 7, 0.16), (2, 3, 0.17), (1, 7, 0.19), (0, 2, 0.26), (5, 7, 0.28),
             (1, 3, 0.29), (1, 5, 0.32), (2, 7, 0.34), (4, 5, 0.35), (1, 2, 0.36),
             (4, 7, 0.37), (0, 4, 0.38), (6, 2, 0.40), (3, 6, 0.52), (6, 0, 0.58),
             (6, 4, 0.93)]
    random.shuffle(edges)
    for v, w, weight in edges:
        graph.add_edge(WeightedEdge(v, w, weight))

    mst = PrimMST(graph)
    mst_edges = mst.edges()

    for edge in mst_edges:
        print(edge)
