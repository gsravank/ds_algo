from QuickUnionPathComp import QuickUnionPathComp
from QuickUnionWeightedPathComp import QuickUnionWeightedPathComp


class Percolate:
    def __init__(self, grid_size):
        self.active = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid_size = grid_size
        self.num_active = 0

        # self.uf_obj = QuickUnionPathComp(self.grid_size * self.grid_size + 2)
        self.uf_obj = QuickUnionWeightedPathComp(self.grid_size * self.grid_size + 2)
        # Connect first virtual object to first row
        for idx in range(1, self.grid_size + 1):
            self.uf_obj.union(idx, 0)

        # Connect last virtual object to last row
        for idx in range(self.grid_size * self.grid_size + 1 - self.grid_size, self.grid_size * self.grid_size + 1):
            self.uf_obj.union(idx, self.grid_size * self.grid_size + 1)

    def cell_idx_to_uf_idx(self, cell_idx):
        return cell_idx + 1

    def cell_idx_to_coordinate(self, cell_idx):
        col_num = cell_idx % self.grid_size
        row_num = int(cell_idx / self.grid_size)
        return row_num, col_num

    def coordinate_to_cell_idx(self, row_num, col_num):
        return (row_num * self.grid_size) + col_num

    def get_neighbors(self, cell_idx):
        row_num, col_num = self.cell_idx_to_coordinate(cell_idx)
        neighbors = list()
        for row_diff, col_diff in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            curr_row_num = row_num + row_diff
            curr_col_num = col_num + col_diff

            if 0 <= curr_col_num <= self.grid_size - 1 and 0 <= curr_row_num <= self.grid_size - 1:
                neighbors.append((curr_row_num, curr_col_num))

        return neighbors

    def activate(self, cell_idx):
        row_num, col_num = self.cell_idx_to_coordinate(cell_idx)
        # print(row_num, col_num)
        if self.active[row_num][col_num] != 1:
            self.active[row_num][col_num] = 1
            self.num_active += 1

            neighbors = self.get_neighbors(cell_idx)
            for (row_num_n, col_num_n) in neighbors:
                if self.active[row_num_n][col_num_n] == 1:
                    neighbor_idx = self.coordinate_to_cell_idx(row_num_n, col_num_n)
                    # print(row_num_n, col_num_n, neighbor_idx)

                    self.uf_obj.union(self.cell_idx_to_uf_idx(cell_idx), self.cell_idx_to_uf_idx(neighbor_idx))

        return

    def is_active(self, cell_idx):
        row_num, col_num = self.cell_idx_to_coordinate(cell_idx)
        return self.active[row_num][col_num] == 1

    def does_it_percolate(self):
        return self.uf_obj.connected(0, self.grid_size * self.grid_size + 1)

    def number_of_active_sites(self):
        return self.num_active
