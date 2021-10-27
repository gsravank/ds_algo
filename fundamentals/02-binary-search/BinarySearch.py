class BinarySearch:
    def __init__(self, array):
        assert len(array) != 0, "Provide a non-empty array"
        self.array = sorted(array)

    def get_print_string(self, idx):
        return f"a[{idx}] = {self.array[idx]}"

    def get_array_print_string(self, indices_to_point=None):
        idx_string = '\t'.join([str(idx) for idx in range(len(self.array))])
        elem_string = '\t'.join([str(elem) for elem in self.array])
        ptr_string = '\t'.join(['|' if indices_to_point is not None and idx in indices_to_point else ' '
                                for idx in range(len(self.array))])
        return '\n'.join([idx_string, elem_string, ptr_string])

    def find(self, element, verbose=False):
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = low + int((high - low) / 2)

            if verbose:
                # print('\t'.join([self.get_print_string(_idx) for _idx in [low, mid, high]]))
                print(self.get_array_print_string([low, mid, high]))
                print('\n')

            if self.array[mid] == element:
                return mid
            elif self.array[mid] < element:
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == "__main__":
    arr = [0, 1, 4, 7, 8, 9, 14, 19, 22, 28, 38, 46, 47, 48]
    bs_obj = BinarySearch(arr)

    print('\t'.join([str(idx) for idx in range(len(arr))]))
    print('\t'.join([str(elem) for elem in arr]))
    print('\n')

    elem = 14

    idx = bs_obj.find(elem, True)
    if idx == -1:
        print(f"{elem} not found")
    else:
        print(f"{elem} found at idx = {idx}")
