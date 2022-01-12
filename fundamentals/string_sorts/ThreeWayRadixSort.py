import random
import string


def char_at(any_string, digit):
    if digit >= len(any_string):
        return '-1'
    else:
        return any_string[digit]


class ThreeWayRadixSort:
    def __init__(self):
        return

    def sort(self, array):
        self._sort(array, 0, len(array) - 1, 0)
        return

    def _sort(self, array, start, end, digit):
        if start >= end:
            return

        # Threeway sort
        lt = start
        gt = end
        pivot_char = char_at(array[start], digit)
        idx = start + 1

        while idx <= gt:
            curr_char = char_at(array[idx], digit)

            if pivot_char > curr_char:
                array[idx], array[lt] = array[lt], array[idx]
                idx += 1
                lt += 1
            elif pivot_char < curr_char:
                array[idx], array[gt] = array[gt], array[idx]
                gt -= 1
            else:
                idx += 1

        # Recursive sort the three pieces
        self._sort(array, start, lt - 1, digit)
        if pivot_char != '-1':
            self._sort(array, lt, gt, digit + 1)
        self._sort(array, gt + 1, end, digit)

        return


if __name__ == '__main__':
    obj = ThreeWayRadixSort()

    arr = list()
    str_len = 5
    # population = random.sample(string.ascii_lowercase, 5)
    population = string.ascii_lowercase[:5]
    # print(sorted(population))
    for _ in range(10):
        arr.append(''.join(random.choices(population, k=random.randint(1, str_len))))

    print('\n'.join(arr) + '\n========\n')
    obj.sort(arr)
    print('\n'.join(arr) + '\n========\n')
