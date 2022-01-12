import math
from collections import deque
from FlowEdge import FlowEdge
from FlowNetwork import FlowNetwork


class FordFulkerson:
    def __init__(self, flow_network, source, target):
        self.value = 0
        self.marked = [False for _ in range(flow_network.number_of_vertices())]
        self.edge_to = [None for _ in range(flow_network.number_of_vertices())]

        while self.has_augmenting_path(flow_network, source, target):
            # Find bottleneck residual capacity along the path
            bottle = math.inf
            curr_vertex = target
            while curr_vertex != source:
                curr_edge = self.edge_to[curr_vertex]
                curr_residual = curr_edge.residual_capacity_to(curr_vertex)
                bottle = min(bottle, curr_residual)
                curr_vertex = curr_edge.other(curr_vertex)

            # Increase flow along the path by this bottleneck value
            curr_vertex = target
            while curr_vertex != source:
                curr_edge = self.edge_to[curr_vertex]
                curr_edge.add_residual_flow_to(curr_vertex, bottle)
                curr_vertex = curr_edge.other(curr_vertex)

            self.value += bottle
        return

    def has_augmenting_path(self, flow_network, source, target):
        # BFS
        self.edge_to = [None for _ in range(flow_network.number_of_vertices())]
        self.marked = [False for _ in range(flow_network.number_of_vertices())]

        queue = deque([])
        queue.appendleft(source)
        self.marked[source] = True
        while len(queue):
            curr_vertex = queue.pop()
            for edge in flow_network.adjacent(curr_vertex):
                other_vertex = edge.other(curr_vertex)
                if not self.marked[other_vertex] and edge.residual_capacity_to(other_vertex) > 0:
                    self.edge_to[other_vertex] = edge
                    self.marked[other_vertex] = True
                    queue.appendleft(other_vertex)

        return self.marked[target]

    def flow(self):
        return self.value

    def in_cut(self, vertex):
        return self.marked[vertex]
