import string
import random


def char_at(any_string, digit):
    if digit >= len(any_string):
        return -1
    else:
        return any_string[digit]


class MSDRadixSort:
    def __init__(self, sorted_keys=None):
        if sorted_keys is None:
            sorted_keys = string.ascii_lowercase

        self.key_to_index_map = dict(zip(sorted_keys, list(range(len(sorted_keys)))))
        self.R = len(self.key_to_index_map)
        self.key_to_index_map[-1] = -1

    def sort(self, array):
        aux = [None for _ in array]
        self._sort(array, 0, len(array) - 1, 0, aux)
        return

    def _sort(self, array, start, end, digit, aux):
        if start >= end:
            return

        count = [0 for _ in range(self.R + 2)]

        # Capture counts based on char at given digit
        for idx in range(start, end + 1):
            curr_string = array[idx]
            char = char_at(curr_string, digit)
            index = self.key_to_index_map[char]

            count[index + 2] += 1

        # Get cumulative counts
        for r in range(self.R + 1):
            count[r + 1] += count[r]

        # Fill up aux based on count array
        for idx in range(start, end + 1):
            aux[count[self.key_to_index_map[char_at(array[idx], digit)] + 1]] = array[idx]
            count[self.key_to_index_map[char_at(array[idx], digit)] + 1] += 1

        # Fill back from aux
        for idx in range(start, end + 1):
            array[idx] = aux[idx - start]

        # Sort recursively for each bucket with the next digit
        for r in range(self.R):
            self._sort(array, start + count[r], start + count[r + 1] - 1, digit + 1, aux)

        return


if __name__ == '__main__':
    obj = MSDRadixSort(sorted_keys=string.ascii_lowercase)

    arr = list()
    str_len = 5
    # population = random.sample(string.ascii_lowercase, 5)
    population = string.ascii_lowercase[:5]
    # print(sorted(population))
    for _ in range(10):
        arr.append(''.join(random.choices(population, k=str_len)))

    print('\n'.join(arr) + '\n========\n')
    obj.sort(arr)
    print('\n'.join(arr) + '\n========\n')
