import random

from LinkedList import Node


class StackLL:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_print_string(self):
        print_strings = list()
        tmp_head = self.head
        while tmp_head is not None:
            print_strings.append(f"| {tmp_head.val} |")
            tmp_head = tmp_head.next_node

        return '\n'.join([' ____ '] + print_strings + [' ---- '])

    def push(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        self.count += 1
        return

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty list!")

        curr_head = self.head
        self.head = self.head.next_node
        self.count -= 1
        return curr_head.val

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count


class StackArr:
    def __init__(self):
        self.items = list()

    def get_print_string(self):
        print_strings = list()
        for val in self.items[::-1]:
            print_strings.append(f"| {val} |")

        return '\n'.join([' ____ '] + print_strings + [' ---- '])

    def is_empty(self):
        return len(self.items) == 0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty list!")

        last_val = self.items.pop()

        return last_val

    def size(self):
        return len(self.items)

    def iterator(self):
        obj = self.ListIterator(self.items)
        return obj

    class ListIterator:
        def __init__(self, items):
            self.curr = 0
            self.arr = items
            return

        def has_next(self):
            return len(self.arr) > self.curr

        def next(self):
            assert self.has_next(), "No elements left to iterate!"
            val = self.arr[self.curr]
            self.curr += 1
            return val


if __name__ == "__main__":
    items = random.sample(list(range(1000)), 10)
    # stack = StackLL()
    stack = StackArr()
    print(' '.join([str(x) for x in items]))
    print('\n')

    for item in items:
        stack.push(item)

    iter_obj = stack.iterator()
    while iter_obj.has_next():
        print(iter_obj.next())
    # iter_obj.next()
    print("\nDone iterating\n")

    print(stack.get_print_string())
    print('\n')

    for _ in range(9):
        _ = stack.pop()

    print(stack.get_print_string())
    print('\n')

    for _ in range(1):
        _ = stack.pop()

    print(stack.get_print_string())




