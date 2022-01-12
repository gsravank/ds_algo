import string
import random


class KeyIndexedCounting:
    def __init__(self, sorted_keys=None):
        if sorted_keys is None:
            sorted_keys = string.ascii_lowercase

        self.key_to_index_map = dict(zip(sorted_keys, list(range(len(sorted_keys)))))
        self.R = len(self.key_to_index_map)

        return

    def sort(self, array, digit=0, start=None, end=None):
        N = len(array)

        if start is None:
            start = 0
        if end is None:
            end = N - 1

        if end <= start:
            return

        count = [0 for _ in range(self.R + 1)]
        aux = [None for _ in range(start, end + 1)]

        # Store counts of each key in count array
        for idx in range(start, end + 1):
            string = array[idx]
            index = self.key_to_index_map[string[digit]]
            count[index + 1] += 1

        # Get cumulative counts to get starting position in the array for each key
        for r in range(self.R):
            count[r + 1] += count[r]

        # Fill up aux with keys based on cumulative counts
        for idx in range(start, end + 1):
            aux[count[self.key_to_index_map[array[idx][digit]]]] = array[idx]
            count[self.key_to_index_map[array[idx][digit]]] += 1

        # Copy aux back to array
        for idx in range(start, end + 1):
            array[idx] = aux[idx]

        return


if __name__ == "__main__":
    obj = KeyIndexedCounting(string.ascii_lowercase)

    arr = random.choices(random.sample(string.ascii_lowercase, 5), k=30)
    print(arr)
    
    obj.sort(arr)
    print(arr)
