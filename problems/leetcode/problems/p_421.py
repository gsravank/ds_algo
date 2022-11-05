class Node:
    def __init__(self, val=None, count=0, left=None, right=None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right
        return

    def __str__(self):
        return f'[{self.val},{self.count}]'


class Solution:
    def getNumBits(self, num):
        count = 0
        while num:
            count += 1
            num = num // 2
        return count

    def isBitSet(self, num, flag):
        return num & flag != 0

    def createBT(self, nums, flag):
        if len(nums) == 0:
            return None, 0
        if flag == 0:
            return Node(nums[0]), 1

        currRoot = Node()
        n0 = [x for x in nums if not self.isBitSet(x, flag)]
        n1 = [x for x in nums if self.isBitSet(x, flag)]

        currRoot.left, c1 = self.createBT(n0, flag // 2)
        currRoot.right, c2 = self.createBT(n1, flag // 2)
        currRoot.count = c1 + c2
        return currRoot, c1 + c2
    
    def printBT(self, root):
        if root is None:
            return
        
        print(root, end=' ')
        self.printBT(root.left)
        self.printBT(root.right)
        return

    def getMaxXor(self, root, currNum, flag):
        # print('\n\n')
        # print(currNum, flag)
        curr = root
        currXor = 0

        while flag:
            currXor *= 2
            # print(curr, flag)
            if self.isBitSet(currNum, flag):
                if curr.left:
                    curr = curr.left
                    currXor += 1
                else:
                    curr = curr.right
            else:
                if curr.right:
                    curr = curr.right
                    currXor += 1
                else:
                    curr = curr.left

            flag = flag // 2
            # print(curr, flag)
            # print()

        foundNum = curr.val
        # print(f"Foundnum: {foundNum} currXor: {currNum ^ foundNum}")

        return currXor

    def findMaximumXOR(self, nums):
        if len(nums) == 1:
            return 0

        max_num = max(nums)
        max_bits = self.getNumBits(max_num)

        # Create BinaryTree
        flag = 1 << max_bits - 1
        root, _ = self.createBT(nums, flag)

        # print(max_num, max_bits)
        # print(root.val, root.count)
        # self.printBT(root)
        # print()

        max_xor = 0
        # Search Max for Each Number in the Tree
        for num in nums:
            max_xor = max(max_xor, self.getMaxXor(root, num, flag))

        return max_xor

obj = Solution()
nums = [3,10,5,25,2,8]
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# nums = [1]
ans = obj.findMaximumXOR(nums)
print(f"Answer: {ans}")
