from Point import Point
from LineSegment import LineSegment
from tqdm import tqdm


class FastCollinearity:
    def __init__(self, points):
        if len(points) <= 3:
            raise Exception("Provide atleast 4 points")

        self.points = points[:]
        self._segments = list()
        self._line_sets = list()

        self._find_segments()

        self._segments = list()
        for x in self._line_sets:
            # print(' '.join([str(y) for y in x]))
            farthest_one, farthest_two = self._find_farthest(x)
            self._segments.append(LineSegment(farthest_one, farthest_two))

        self._remove_duplicate_segments()

    def _remove_duplicate_segments(self):
        fin_segments = list()
        for segment in self._segments:
            if segment not in fin_segments:
                fin_segments.append(segment)
        self._segments = fin_segments
        return

    def _find_farthest(self, list_of_points):
        pairs = list()
        for idx in range(len(list_of_points) - 1):
            for jdx in range(idx + 1, len(list_of_points)):
                pairs.append((list_of_points[idx], list_of_points[jdx]))
        sorted_pairs = sorted(pairs, key=lambda pair: (pair[0].x - pair[1].x)**2 + (pair[0].y - pair[1].y)**2)

        return sorted_pairs[-1]  # , [x for x in list_of_points if x not in sorted_pairs[-1]]

    def _segment_present_for_pair(self, p, q):
        for each_set in self._line_sets:
            found_p = False
            found_q = False
            for point in each_set:
                if point == p:
                    found_p = True
                if point == q:
                    found_q = True

                if found_p and found_q:
                    return True

        return False

    def _find_segments(self):
        n = len(self.points)

        for idx in tqdm(range(n)):
            # Fix current point
            curr_point = self.points[idx]

            # Get other points and their slopes with fixed point
            other_points_slopes = list()
            for jdx, other_point in enumerate(self.points):
                if jdx != idx:
                    # if not self._segment_present_for_pair(curr_point, other_point):
                    if True:
                        other_points_slopes.append([other_point, curr_point.slope_to(other_point)])

            if len(other_points_slopes) < 3:
                continue
            # else:
            #     print(str(curr_point) + ' - ' + ' '.join([str(_y[0]) for _y in other_points_slopes]))

            # Sort other points based on slope with fixed point
            sorted_other_points_slopes = sorted(other_points_slopes, key=lambda x: x[1])
            # for _x in sorted_other_points_slopes:
            #     print(_x[0], _x[1])

            # Check for sequence of points with the same slope
            curr_line_sets = list()
            poss_line_set = [sorted_other_points_slopes[0][0]]
            for idx, jdx in zip(range(len(sorted_other_points_slopes) - 1), range(1, len(sorted_other_points_slopes))):
                if sorted_other_points_slopes[jdx][1] == sorted_other_points_slopes[idx][1]:
                    poss_line_set.append(sorted_other_points_slopes[jdx][0])
                else:
                    if len(poss_line_set) >= 3:
                        curr_line_sets.append(poss_line_set + [curr_point])
                    poss_line_set = [sorted_other_points_slopes[jdx][0]]

            if len(poss_line_set) >= 3:
                curr_line_sets.append(poss_line_set + [curr_point])

            # if len(curr_line_sets):
            #     for each_set in curr_line_sets:
            #         print([str(x) for x in each_set])
            #     print('\n\n')

            self._line_sets.extend(curr_line_sets)

        return

    def number_of_segments(self):
        return len(self._segments)

    def segments(self):
        return self._segments
