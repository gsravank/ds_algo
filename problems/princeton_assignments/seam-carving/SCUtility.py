from Picture import Picture
from SeamCarver import SeamCarver
import matplotlib.pyplot as plt
import random
import numpy as np


class SCUtility:
    def __init__(self):
        return

    @staticmethod
    def random_picture(width, height):
        picture = Picture(width=width, height=height)
        for col in range(width):
            for row in range(height):
                picture.set(row, col, random.random(), random.random(), random.random())
        return picture

    @staticmethod
    def to_energy_matrix(seam_carver):
        energy_matrix = [[0.0 for _ in range(seam_carver.width())] for _ in range(seam_carver.height())]
        for col in range(seam_carver.width()):
            for row in range(seam_carver.height()):
                energy_matrix[row][col] = seam_carver.energy(col, row)

        return energy_matrix
    
    @staticmethod
    def double_to_picture(gray_matrix):
        height = len(gray_matrix)
        width = len(gray_matrix[0])

        pic = Picture(width=width, height=height)

        max_value = 0
        for col in range(1, width - 1):
            for row in range(1, height - 1):
                if gray_matrix[row][col] > max_value:
                    max_value = gray_matrix[row][col]

        if max_value == 0:
            return pic

        for col in range(width):
            for row in range(height):
                normalized_gray = gray_matrix[row][col] / float(max_value)
                if normalized_gray > 1.0:
                    normalized_gray = 1.0
                pic.set(row, col, normalized_gray, normalized_gray, normalized_gray)

        return pic

    @staticmethod
    def show_energy(seam_carver):
        SCUtility.double_to_picture(SCUtility.to_energy_matrix(seam_carver)).show()

    @staticmethod
    def seam_overlay(picture, horizontal_flag, seam_indices):
        overlaid = Picture(width=picture.width(), height=picture.height())
        width = picture.width()
        height = picture.height()

        for col in range(width):
            for row in range(height):
                r, g, b = picture.get(row, col)
                overlaid.set(col, row, r, g, b)

        if horizontal_flag:
            for col in range(width):
                overlaid.set(seam_indices[col], col, 1.0, 0.0, 0.0)
        else:
            for row in range(height):
                overlaid.set(row, seam_indices[row], 1.0, 0.0, 0.0)

        return overlaid
