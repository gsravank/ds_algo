from Point import Point


class LineSegment:
    def __init__(self, p, q):
        if p is None or q is None:
            raise Exception("Illegal argument given to line segment")

        self.p = p
        self.q = q

    def __str__(self):
        return f"{self.p} -> {self.q}"

    def __eq__(self, other):
        return (self.p == other.p and self.q == other.q) or (self.p == other.q and self.q == other.p)