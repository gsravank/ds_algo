import bisect


def read_lines(filename):
    lines = list()
    with open(filename, 'r') as f:
        for line in f.readlines():
            if len(line.strip()):
                lines.append(line.strip())
    return lines


def write_lines(lines, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))


def number_elems_geq(elems, value):
    if value < elems[0]:
        return len(elems)
    if value > elems[-1]:
        return 0
    idx = bisect.bisect_left(elems, value)
    return len(elems) - idx