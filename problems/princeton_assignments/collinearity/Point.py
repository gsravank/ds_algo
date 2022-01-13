import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False

        if self.y < other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def slope_to(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return -math.inf
            else:
                return math.inf
        else:
            return float(other.y - self.y) / (other.x - self.x)

    def slope_order(self, p1, p2):
        return self.slope_to(p1) - self.slope_to(p2)
