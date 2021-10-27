"""
Problems which use binary search style algorithm
"""
from BinarySearch import BinarySearch


class BinarySearchAlt(BinarySearch):
    def find_highest_lower_than(self, value, verbose=False):
        if self.array[0] >= value:
            return -1
        if self.array[-1] < value:
            return len(self.array) - 1

        low = 0
        high = len(self.array) - 1
        mid = int((low + high) / 2)

        while low < high - 1:
            mid = int((low + high) / 2)

            if verbose:
                print(self.get_array_print_string([low, mid, high]))
                print('\n')

            if self.array[mid] >= value:
                if mid == 0:
                    return -1
                else:
                    high = mid - 1
            else:
                if mid == len(self.array) - 1:
                    return len(self.array) - 1
                else:
                    low = mid

        if verbose:
            print(self.get_array_print_string([low, high]))
            print('\n')

        if low == high:
            return low
        else:
            if self.array[high] < value:
                return high
            else:
                return low

    def find_highest_lower_than_elegant(self, value, verbose=False):
        if self.array[0] >= value:
            return -1
        if self.array[-1] < value:
            return len(self.array) - 1

        answer = 0
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = low + int((high - low) / 2)
            if verbose:
                print(self.get_array_print_string([low, mid, high]))
                print('\n')

            if self.array[mid] >= value:
                high = mid - 1
            else:
                answer = mid
                low = mid + 1

        if verbose:
            print(self.get_array_print_string([low, high]))
            print('\n')
        return answer


if __name__ == "__main__":
    arr = [0, 1, 4, 7, 8, 9, 14, 19, 22, 28, 38, 46, 47, 48]
    # arr = [0, 14, 14, 14, 50]
    bs_obj = BinarySearchAlt(arr)

    print('\t'.join([str(idx) for idx in range(len(arr))]))
    print('\t'.join([str(elem) for elem in arr]))
    print('\n')

    elem = 14

    idx = bs_obj.find_highest_lower_than_elegant(elem, True)
    if idx == -1:
        print(f"No element lower than {elem} found in the array")
    else:
        print(f"a[{idx}] = {arr[idx]} < {elem}")
