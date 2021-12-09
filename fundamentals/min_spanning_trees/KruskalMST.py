from EdgeWeightedGraph import EdgeWeightedGraph
import random
from WeightedEdge import WeightedEdge
from fundamentals.union_find.QuickUnionWeightedPathComp import QuickUnionWeightedPathComp


class KruskalMST:
    def __init__(self, ewgraph):
        self.mst_weight = 0
        self.mst_edges = list()

        sorted_edges = sorted(ewgraph.edges(), key=lambda e: e.weight())
        num_vertices = ewgraph.num_vertices()
        uf = QuickUnionWeightedPathComp(num_vertices)
        
        for edge in sorted_edges:
            v = edge.either()
            w = edge.other(v)
            
            if not uf.connected(v, w):
                uf.union(v, w)
                self.mst_edges.append(edge)
                self.mst_weight += edge.weight()

                print(self.mst_edges)
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

    mst = KruskalMST(graph)
    mst_edges = mst.edges()

    for edge in mst_edges:
        print(edge)
