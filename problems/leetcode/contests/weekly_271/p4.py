class Solution:
    def getCumSumTill(self, cumsum_arr, i, n):
        if i <= -1:
            return 0
        elif i >= n:
            return cumsum_arr[-1]
        else:
            return cumsum_arr[i]

    def getMinGreaterThan(self, positions, value):
        n = len(positions)
        if value < positions[0]:
            return 0, 0
        elif value == positions[0]:
            return 0, 1
        elif value == positions[n - 1]:
            return n - 1, 1
        elif value > positions[n - 1]:
            return n, 0

        low = 0
        high = n - 1
        answer = 0

        while low <= high:
            mid = low + int((high - low) / 2)
            if positions[mid] >= value:
                high = mid - 1
                answer = mid
            else:
                low = mid + 1

        return answer, 1 if positions[answer] == value else 0

    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        fruit_positions = [x[0] for x in fruits]
        cum_sum = list()
        curr_sum = 0
        for idx in range(n):
            curr_sum += fruits[idx][1]
            cum_sum.append(curr_sum)

        left_min_pos = startPos - k
        right_max_pos = startPos + k

        left_min_fruit_pos, lmin_flag = self.getMinGreaterThan(fruit_positions, left_min_pos)
        left_max_fruit_pos, lmax_flag = self.getMinGreaterThan(fruit_positions, startPos)

        right_min_fruit_pos, rmin_flag = self.getMinGreaterThan(fruit_positions, startPos)
        right_max_fruit_pos, rmax_flag = self.getMinGreaterThan(fruit_positions, right_max_pos)

        if left_min_fruit_pos == left_max_fruit_pos:
            left_sum = 0
        else:
            s1 = self.getCumSumTill(cum_sum, left_min_fruit_pos - lmin_flag)
            s2 = self.getCumSumTill(cum_sum, left_max_fruit_pos - lmax_flag)
            left_sum = s2 - s1

        if right_min_fruit_pos == right_max_fruit_pos:
            right_sum = 0
        else:
            s1 = self.getCumSumTill(cum_sum, right_min_fruit_pos - rmin_flag)
            s2 = self.getCumSumTill(cum_sum, right_max_fruit_pos - rmax_flag)

            right_sum = s2 - s1

        return max(right_sum, left_sum)


obj = Solution()
print(obj.getMinGreaterThan([0,1,2,3,4,5], 0.5))

"""
[[2,8],[6,3],[8,6]]
5
4
[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
5
4
[[0,3],[6,4],[8,5]]
3
2
"""