"""
Suppose you are given a permutation p of the integers 1 to n,
and seek to sort them to be in increasing order [1, . . . , n].
The only operation at your disposal is reverse(p,i,j),
which reverses the elements of a subsequence p i , . . . , pj
in the permutation. For the permutation [1, 4, 3, 2, 5]
one reversal (of the second through fourth elements) suﬃces to sort.

• Show that it is possible to sort any permutation using O(n) reversals.

• Now suppose that the cost of reverse(p,i,j) is equal to its length,
the number of elements in the range, | j − i | + 1.
Design an algorithm that sorts p in O(n log 2 n) cost.
Analyze the running time and cost of your algorithm and prove correctness.
"""
import random

def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return


class SortByReverse:
    def __init(self):
        return

    def sort(self, array):
        self._sort(array, 0, len(array) - 1)
        return array

    def _sort(self, array, low, high):
        if low >= high:
            return
        if high == low + 1:
            if array[low] > array[high]:
                reverse(array, low, high)
            return

        # Sort recursively left and right sub parts
        mid = 1 + (low + high) // 2
        self._sort(array, low, mid - 1)
        self._sort(array, mid, high)

        # Merge, which is also done recursively
        self._merge(array, low, mid, high)

        return

    def _merge(self, array, low, mid, high):
        # print(low, high, array)
        if low >= high:
            return
        if high == low + 1:
            if array[low] > array[high]:
                reverse(array, low, high)
            return

        # mid = 1 + (low + high) // 2
        numLeftElems = mid - low
        leftIdx, rightIdx = low, mid
        while numLeftElems:
            if array[leftIdx] <= array[rightIdx]:
                leftIdx += 1
            else:
                rightIdx += 1
            numLeftElems -= 1
        if leftIdx == mid:
            # No need to merge
            pass
        else:
            revSize = rightIdx - leftIdx
            leftRevSize = mid - leftIdx
            rightRevSize = rightIdx - mid
            # print(leftRevSize, rightRevSize)
            reverse(array, leftIdx, rightIdx - 1)
            reverse(array, leftIdx, leftIdx + rightRevSize - 1)
            reverse(array, leftIdx + rightRevSize, rightIdx - 1)

            self._merge(array, low, leftIdx, mid - 1)
            self._merge(array, mid, rightIdx, high)
        return


if __name__ == '__main__':
    numbers = list(range(1, 20))
    random.seed(0)
    random.shuffle(numbers)
    print(numbers)

    sortObj = SortByReverse()
    numbers = sortObj.sort(numbers)
    print(numbers)

    # numbers = [0,10,22,35,2,11,20,33]
    # sortObj = SortByReverse()
    # low = 0
    # high = len(numbers) - 1
    # mid = 4
    # sortObj._merge(numbers, low, mid, high)