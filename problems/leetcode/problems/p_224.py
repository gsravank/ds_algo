class Solution:
    def compute(self, items):
        result, curr, last = 0, 0, 0
        op = '+'
        found = False
        stack = list()
        count = 0

        for idx, item in enumerate(items):
            if item == '(':
                found = True
                count += 1
            elif item == ')':
                count -= 1

            if found:
                stack.append(item)

            if found and count == 0:
                found = False
                curr = self.compute(stack[1:-1])
                stack = list()

            if not found:
                if item.isdigit():
                    curr = 10 * curr + ord(item) - ord('0')

                if (not item.isdigit() and not item == " ") or idx == len(items) - 1:
                    if op == '-':
                        curr = -curr
                    result += last
                    last = curr
                    curr = 0
                    op = item

        result += last
        return result

    def calculate(self, s: str) -> int:
        # s = ''.join(['(', s, ')'])
        items = s.split()
        result = self.compute(items)
        return result


obj = Solution()
result = obj.compute(['(', '1', '+', '1', ')'])
print(result)