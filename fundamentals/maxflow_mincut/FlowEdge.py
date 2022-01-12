class FlowEdge:
    def __init__(self, v, w, capacity):
        self.v = v
        self.w = w
        self.capacity_value = capacity
        self.flow_value = 0.0

    def from_vertex(self):
        return self.v

    def to_vertex(self):
        return self.w

    def other_vertex(self, v):
        if self.v == v:
            return self.w
        else:
            return self.v

    def capacity(self):
        return self.capacity_value

    def flow(self):
        return self.flow_value

    def residual_capacity_to(self, v):
        if v == self.w:
            return self.capacity_value - self.flow_value
        else:
            return self.flow_value

    def add_residual_flow_to(self, v, delta):
        if v == self.w:
            self.flow_value += delta
        else:
            self.flow_value -= delta
        return

    def __repr__(self):
        return f"{self.v}-{self.flow_value}/{self.capacity_value}->{self.w}"
