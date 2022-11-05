from collections import deque, defaultdict
from heapq import heappush


class Item:
    def __init__(self, dist, price, row, col):
        self.dist = dist
        self.price = price
        self.row = row
        self.col = col

    def __lt__(self, other):
        if self.dist < other.dist:
            return True
        elif self.dist == other.dist:
            if self.price < other.price:
                return True
            elif self.price == other.price:
                if self.row < other.row:
                    return True
                elif self.row == other.row:
                    if self.col < other.col:
                        return True
                    elif self.col == other.col:
                        return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.dist == other.dist and self.price == other.price and self.row == other.row and self.col == other.col

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


class Solution:
    def get_cell_num(self, r, c, m, n):
        return r * n + c

    def get_row_col(self, cell_num, m, n):
        c = cell_num % n
        r = cell_num // n
        return r, c

    def highestRankedKItems(self, grid, pricing, start, k):
        adjacent = defaultdict(lambda: list())
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                cell_num = self.get_cell_num(r, c, m, n)

                for r_diff, c_diff in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if r_diff == 0 and c_diff == 0:
                        pass
                    else:
                        n_r = r + r_diff
                        n_c = c + c_diff
                        n_cell_num = self.get_cell_num(n_r, n_c, m, n)

                        if 0 <= n_r <= m - 1 and 0 <= n_c <= n - 1:
                            if grid[n_r][n_c] != 0:
                                adjacent[cell_num].append(n_cell_num)
                                adjacent[n_cell_num].append(cell_num)

        # BFS
        visited = defaultdict(lambda: False)
        start_cell_num = self.get_cell_num(start[0], start[1], m, n)
        visited[start_cell_num] = True
        queue_vertices = deque([])
        queue_vertices.append([start_cell_num, 0])
        done = False
        min_pq = list() if grid[start[0]][start[1]] == 0 else [Item(0, grid[start[0]][start[1]], start[0], start[1])]

        while len(queue_vertices):
            curr_tup = queue_vertices.pop()
            curr_vertex = curr_tup[0]
            curr_dist = curr_tup[1]
            for neighbor in adjacent[curr_vertex]:
                if not visited[neighbor]:
                    queue_vertices.appendleft([neighbor, curr_dist + 1])
                    visited[neighbor] = True

                    n_r, n_c = self.get_row_col(neighbor, m, n)
                    price = grid[n_r][n_c]
                    if pricing[0] <= price <= pricing[1]:
                        item = Item(curr_dist + 1, price, n_r, n_c)
                        heappush(min_pq, item)

        return [[x.row, x.col] for x in sorted(min_pq)[:k]]



obj = Solution()
grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
pricing = [2, 5]
start = [0,0]
k = 3

ans = obj.highestRankedKItems(grid, pricing, start, k)
print(ans)


"""
0
1
2
5
8
"""