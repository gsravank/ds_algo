class WeightedDiEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self._weight = weight
        
    def weight(self):
        return self._weight
    
    def from_vertex(self):
        return self.v
    
    def to_vertex(self):
        return self.w
    
    def __repr__(self):
        return f"{self.v}-({self._weight})->{self.w}"

    def __eq__(self, other):
        return self._weight == other.weight()

    def __lt__(self, other):
        return self._weight < other.weight()

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return self._weight > other.weight()

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

