import random

from utils.DSUtils import get_array_print_string_as_complete_binary_tree


class MaxHeap:
    def __init__(self, items):
        self.array = items
        self.size = len(items)
        self.build_max_heap()
        return

    def _parent(self, idx):
        return int((idx - 1) / 2)

    def _left_child(self, idx):
        return 2 * idx + 1

    def _right_child(self, idx):
        return 2 * idx + 2

    def build_max_heap(self):
        # for idx in range(int(self.size / 2) - 1, -1, -1):
        for idx in range(int(self.size / 2) - 1, -1, -1):
            self.bubble_down(idx)
            # print(get_array_print_string_as_complete_binary_tree(self.array))

        return

    def bubble_up(self, idx):
        while idx != 0:
            parent_idx = self._parent(idx)
            if self.array[parent_idx] < self.array[idx]:
                self.swap(parent_idx, idx)
                idx = parent_idx
            else:
                break
        return

    def bubble_down(self, idx):
        while True:
            left_child = self._left_child(idx)
            right_child = self._right_child(idx)

            required_indices = [idx]
            if left_child < self.size:
                required_indices.append(left_child)
            if right_child < self.size:
                required_indices.append(right_child)

            if len(required_indices) == 1:
                # Both left and right children are not part of the heap
                break

            max_index = required_indices[0]
            for curr_index in required_indices[1:]:
                if self.array[curr_index] > self.array[max_index]:
                    max_index = curr_index

            # sorted_required_indices = sorted(required_indices, key=lambda i: self.array[i])
            # max_index = sorted_required_indices[-1]

            if max_index == idx:
                # Current root is itself the maximum. Nothing left to do
                break
            else:
                self.swap(idx, max_index)
                idx = max_index
        return

    def insert(self, key):
        self.array.append(key)
        self.size += 1
        self.bubble_up(self.size - 1)
        return

    def max(self):
        return self.array[0]

    def delete_max(self):
        self.swap(0, self.size - 1)
        self.size -= 1
        self.bubble_down(0)
        return

    def size(self):
        return self.size

    def __str__(self):
        return get_array_print_string_as_complete_binary_tree(self.array)

    def swap(self, idx, jdx):
        self.array[idx], self.array[jdx] = self.array[jdx], self.array[idx]
        return


if __name__ == "__main__":
    items = list(range(7))
    items = random.sample(list(range(100)), 15)
    random.shuffle(items)

    print(get_array_print_string_as_complete_binary_tree(items))
    # print('\n\n\n\n')
    max_heap = MaxHeap(items)
    print('\n\n\n\n')
    print(max_heap)

