import math

def lis(nums, k=math.inf):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        if tails[i] == 0:
            if i == 0:
                tails[i] = x
                size = max(i + 1, size)
            else:
                if x - tails[i-1] <= k:
                    tails[i] = x
                    size = max(i + 1, size)
        else:
            tails[i] = x
            size = max(i + 1, size)

        #        tails[i] = x
#        size = max(i + 1, size)
        print(tails, size)
    return size

arr = [1,3,3,4]
print(lis(arr, 1))