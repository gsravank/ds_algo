import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class Picture:
    def __init__(self, filename=None, width=None, height=None):
        if filename is None:
            if width is None or height is None:
                raise Exception("Provide filename or dimensions")

            # self.image = np.zeros((height, width, 3)).astype(int)
            self.image = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
        else:
            image = mpimg.imread(filename)
            self.image = [[None for _ in range(len(image[0]))] for _ in range(len(image))]
            for row in range(len(image)):
                for col in range(len(image[0])):
                    tmp_rgb = image[row][col]
                    self.image[row][col] = [tmp_rgb[0], tmp_rgb[1], tmp_rgb[2]]

            # self.image = mpimg.imread(filename)
            # if not filename.strip().endswith(".png"):
            #     for row in range(self.height()):
            #         for col in range(self.width()):
            #             r, g, b = self.get(row, col)
            #             self.set(row, col, float(r) / 255.0, float(g) / 255.0, float(b) / 255.0)

    def show(self):
        plt.imshow(self.image)
        plt.show()
        return

    def save(self, filename):
        mpimg.imsave(filename, self.image)
        return

    def get(self, row, col):
        return self.image[row][col]
    
    def set(self, row, col, red, green, blue):
        # assert 0 <= red <= 1 and 0 <= green <= 1 and 0 <= blue <= 1
        assert 0 <= row < len(self.image) and 0 <= col < len(self.image[0])
        
        self.image[row][col] = np.array([red, green, blue])
        
    def width(self):
        return len(self.image[0])

    def height(self):
        return len(self.image)
