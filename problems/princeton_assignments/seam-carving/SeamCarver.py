from Picture import Picture
import math


class SeamCarver:
    def __init__(self, picture):
        self.pic = picture
        self.current_pic = self.pic

    def picture(self):
        return self.current_pic

    def width(self):
        return self.current_pic.width()

    def height(self):
        return self.current_pic.height()

    def energy(self, col, row):
        width = self.current_pic.width()
        height = self.current_pic.height()

        if col == 0 or col == width - 1 or row == 0 or row == height - 1:
            return 1000.0

        rgb = self.current_pic.get(row, col)
        rgb_x_prev = self.current_pic.get(row, col - 1)
        rgb_x_next = self.current_pic.get(row, col + 1)
        rgb_y_prev = self.current_pic.get(row + 1, col)
        rgb_y_next = self.current_pic.get(row - 1, col)

        x_grad = 0.0
        y_grad = 0.0
        for i in range(3):
            x_grad += math.pow(rgb_x_next[i] - rgb_x_prev[i], 2.0)
        for i in range(3):
            y_grad += math.pow(rgb_y_next[i] - rgb_y_prev[i], 2.0)

        return math.sqrt(x_grad + y_grad)

    def find_horizontal_seam(self):
        width = self.width()
        height = self.height()

        distance_to = [[math.inf for _ in range(width)] for _ in range(height)]
        vertex_to = [[None for _ in range(width)] for _ in range(height)]

        for row in range(height):
            distance_to[row][0] = self.energy(0, row)
        for col in range(1, width):
            for row in range(height):
                min_value = distance_to[row][col]
                curr_energy = self.energy(col, row)
                prev_col_choices = [row-1, row, row+1]
                for choice in prev_col_choices:
                    if 0 <= choice < height:
                        curr_distance = distance_to[choice][col - 1] + curr_energy
                        if curr_distance < min_value:
                            min_value = curr_distance
                            distance_to[row][col] = min_value
                            vertex_to[row][col] = choice

        # Find least distance in the last row
        end_vertex = None
        min_distance = math.inf
        for row in range(height):
            if distance_to[row][width - 1] < min_distance:
                min_distance = distance_to[row][width - 1]
                end_vertex = row

        # Find shortest path
        path = [end_vertex]
        for col in range(width - 1, 0, -1):
            path.append(vertex_to[path[-1]][col])

        return path[::-1]

    def find_vertical_seam(self):
        width = self.width()
        height = self.height()

        distance_to = [[math.inf for _ in range(width)] for _ in range(height)]
        vertex_to = [[None for _ in range(width)] for _ in range(height)]

        for col in range(width):
            distance_to[0][col] = self.energy(col, 0)
        for row in range(1, height):
            for col in range(width):
                min_value = distance_to[row][col]
                curr_energy = self.energy(col, row)
                prev_row_choices = [col-1, col, col+1]
                for choice in prev_row_choices:
                    if 0 <= choice < width:
                        curr_distance = distance_to[row-1][choice] + curr_energy
                        if curr_distance < min_value:
                            min_value = curr_distance
                            distance_to[row][col] = min_value
                            vertex_to[row][col] = choice

        # Find least distance in the last row
        end_vertex = None
        min_distance = math.inf
        for col in range(width):
            if distance_to[height - 1][col] < min_distance:
                min_distance = distance_to[height - 1][col]
                end_vertex = col

        # Find shortest path
        path = [end_vertex]
        for row in range(height - 1, 0, -1):
            path.append(vertex_to[row][path[-1]])

        return path[::-1]

    def remove_horizontal_seam(self, row_indices):
        width = self.width()
        height = self.height()

        new_picture = Picture(width=width, height=height-1)
        for col in range(width):
            new_row = 0
            for row in range(height):
                if row_indices[col] != row:
                    r, g, b = self.current_pic.get(row, col)
                    new_picture.set(new_row, col, r, g, b)
                    new_row += 1

        self.current_pic = new_picture
        return

    def remove_vertical_seam(self, col_indices):
        width = self.width()
        height = self.height()

        new_picture = Picture(width=width - 1, height=height)
        for row in range(height):
            new_col = 0
            for col in range(width):
                if col_indices[row] != col:
                    r, g, b = self.current_pic.get(row, col)
                    new_picture.set(row, new_col, r, g, b)
                    new_col += 1

        self.current_pic = new_picture
        return
