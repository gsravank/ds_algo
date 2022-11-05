"""
Design a stack S that supports S.push(x), S.pop(), and S.findmin(), which
returns the minimum element of S. All operations should run in constant time
"""


class Stack:
    def __init__(self):
        self.items = list()
        self.minimums = list()
        return

    def push(self, item):
        if len(self.minimums):
            curr_min = min(item, self.minimums[-1])
        else:
            curr_min = item

        self.items.append(item)
        self.minimums.append(curr_min)
        return

    def pop(self):
        self.minimums.pop()
        return self.items.pop()

    def find_min(self):
        if len(self.minimums):
            return self.minimums[-1]
        else:
            return None


