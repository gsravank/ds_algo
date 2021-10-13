import random

from DoesItPercolate import Percolate
from utils.DSUtils import print_2d_matrix

grid_size = 10

perc_obj = Percolate(grid_size)
# print(perc_obj.uf_obj.items)
# print(perc_obj.does_it_percolate())
# print('\n')

for idx in random.sample(list(range(grid_size * grid_size)), 58):
    print(idx)

    perc_obj.activate(idx)
    print_2d_matrix(perc_obj.active, {1: 1, 0: ' '})
    print('\n')
    # print(perc_obj.uf_obj.items)
    print(perc_obj.does_it_percolate())
    print('\n======')

    if perc_obj.does_it_percolate():
        break

print(perc_obj.number_of_active_sites())