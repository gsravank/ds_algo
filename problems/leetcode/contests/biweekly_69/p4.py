"""
https://leetcode.com/contest/biweekly-contest-69/problems/stamping-the-grid/
"""

class Solution:
    def canBePlaced(self, x1, x2, y1, y2, x, y):
        return y <= (y1 + y2 + 1) and x <= (x1 + x2 + 1)

    def possibleToStamp(self, grid, stampHeight, stampWidth):
        m = len(grid)
        n = len(grid[0])

        ltor = [[None for _ in range(n)] for _ in range(m)]
        rtol = [[None for _ in range(n)] for _ in range(m)]
        utod = [[None for _ in range(n)] for _ in range(m)]
        dtou = [[None for _ in range(n)] for _ in range(m)]

        for row in range(m):
            prev_val = -1
            for col in range(n):
                if grid[row][col] == 1:
                    prev_val = col
                ltor[row][col] = prev_val

        for row in range(m):
            prev_val = n
            for col in range(n-1, -1, -1):
                if grid[row][col] == 1:
                    prev_val = col
                rtol[row][col] = prev_val

        for col in range(n):
            prev_val = -1
            for row in range(m):
                if grid[row][col] == 1:
                    prev_val = row
                utod[row][col] = prev_val

        for col in range(n):
            prev_val = m
            for row in range(m-1, -1, -1):
                if grid[row][col] == 1:
                    prev_val = row

                dtou[row][col] = prev_val

        print(ltor)
        print(rtol)
        print(utod)
        print(dtou)
        print('\n')

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    x1 = col - ltor[row][col] - 1
                    x2 = rtol[row][col] - col - 1

                    y1 = row - utod[row][col] - 1
                    y2 = dtou[row][col] - row - 1

                    print(row, col, x1, x2, y1, y2)

                    if not self.canBePlaced(x1, x2, y1, y2, stampWidth, stampHeight):
                        return False

        return True

grid = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]
]
grid = [[1]]
sh = 2
sw = 1
obj = Solution()
print(f"Answer = {obj.possibleToStamp(grid, sh, sw)}")