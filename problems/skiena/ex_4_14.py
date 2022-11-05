"""
4-14. [5] Given a list I of n intervals, specified as (xi, yi) pairs, return a list where
the overlapping intervals are merged. For I = {(1, 3), (2, 6), (8, 10), (7, 18)} the
output should be {(1, 6), (7, 18)}. Your algorithm should run in worst-case
O(n log n) time complexity.

"""


def checkOverlap(I1, I2):
    if I1[0] > I2[0]:
        I1, I2, = I2, I1

    return I1[1] >= I2[0]


def mergeIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    final = list()
    start, end = intervals[0]

    for idx in range(1, len(intervals)):
        if checkOverlap((start, end), intervals[idx]):
            end = max(end, intervals[idx][1])
        else:
            final.append((start, end))
            start, end = intervals[idx]

        if idx == len(intervals) - 1:
            final.append((start, end))
    return final


ints = [(1, 3), (2, 6), (8, 10), (7, 18), (9, 15), (19, 20)]
merged = mergeIntervals(ints)

print(merged)
