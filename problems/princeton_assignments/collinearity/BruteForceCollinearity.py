from Point import Point
from LineSegment import LineSegment
from tqdm import tqdm


class BruteForce:
    def __init__(self, points):
        if len(points) <= 3:
            raise Exception("Provide atleast 4 points")
        self.points = points[:]
        self._segments = list()

        self._find_segments()

    def _check_collinearity(self, p, q, r, s):
        return p.slope_to(q) == p.slope_to(r) == p.slope_to(s)

    def _find_farthest(self, list_of_points):
        pairs = list()
        for idx in range(len(list_of_points) - 1):
            for jdx in range(idx + 1, len(list_of_points)):
                pairs.append((list_of_points[idx], list_of_points[jdx]))
        sorted_pairs = sorted(pairs, key=lambda pair: (pair[0].x - pair[1].x)**2 + (pair[0].y - pair[1].y)**2)

        return sorted_pairs[-1]

    def _find_segments(self):
        n = len(self.points)

        for idx in tqdm(range(n-3)):
            for jdx in range(idx + 1, n-2):
                for kdx in range(jdx + 1, n-1):
                    for ldx in range(kdx + 1, n):
                        p, q, r, s = self.points[idx], self.points[jdx], self.points[kdx], self.points[ldx]
                        if self._check_collinearity(p, q, r, s):
                            farthest_one, farthest_two = self._find_farthest([p, q, r, s])
                            curr_line_segment = LineSegment(farthest_one, farthest_two)
                            self._segments.append(curr_line_segment)

        return

    def number_of_segments(self):
        return len(self._segments)

    def segments(self):
        return self._segments
