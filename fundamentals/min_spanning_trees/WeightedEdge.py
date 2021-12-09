class WeightedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self._weight = weight

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v:
            return self.w
        else:
            return self.v

    def weight(self):
        return self._weight

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

    def __repr__(self):
        return f"{self.v}--({self._weight})--{self.w}"

    def __hash__(self):
        return hash(f"{self.v}-{self.w}-{self._weight}")
