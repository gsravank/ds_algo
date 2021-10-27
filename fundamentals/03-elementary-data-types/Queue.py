import random

from LinkedList import Node


class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get_print_string(self):
        tmp_head = self.head
        print_items = list()
        while tmp_head is not None:
            print_items.append(str(tmp_head.get_val()))
            tmp_head = tmp_head.get_next_node()
        return ' <- '.join(print_items)

    def is_empty(self):
        return self.count == 0

    def enqueue(self, val):
        new_node = Node(val, None)
        if self.tail is not None:
            self.tail.next_node = new_node
        self.tail = new_node
        self.count += 1
        if self.head is None:
            self.head = self.tail
        return

    def dequeue(self):
        if self.is_empty():
            raise Exception("Removing from an empty queue!")

        curr_node = self.head
        self.head = curr_node.next_node
        self.count -= 1

        if self.head is None:
            self.tail = None

        return curr_node.val


class QueueArr:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.capacity = 1
        self.items = [None for _ in range(self.capacity)]
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def _upsize(self):
        if self.head != self.tail:
            return

        new_capacity = self.capacity * 2
        new_items = [None for _ in range(new_capacity)]

        curr_head = self.head
        idx = 0
        done = False
        while not done:
            new_items[idx] = self.items[curr_head]
            idx += 1
            curr_head = (curr_head + 1) % self.capacity

            if curr_head == self.head:
                done = True

        self.head = 0
        self.tail = self.capacity
        self.capacity *= 2
        self.items = new_items
        return

    def _downsize(self):
        if self.capacity == 1 or self.count > int(self.capacity / 4):
            return

        new_capacity = int(self.capacity / 2)
        new_items = [None for _ in range(new_capacity)]

        curr_head = self.head
        idx = 0
        done = curr_head == self.tail
        while not done:
            new_items[idx] = self.items[curr_head]
            idx += 1
            curr_head = (curr_head + 1) % self.capacity

            if curr_head == self.tail:
                done = True

        self.head = 0
        self.capacity = new_capacity
        self.tail = int(new_capacity / 2)
        self.items = new_items

        return

    def get_print_string(self):
        curr_head = self.head
        print_strings = list()
        while curr_head != self.tail:
            print_strings.append(str(self.items[curr_head]))
            curr_head = (curr_head + 1) % self.capacity
        return ' <- '.join(print_strings)

    def enqueue(self, val):
        self.items[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

        self._upsize()

        return

    def dequeue(self):
        if self.is_empty():
            raise Exception("Removing from an empty queue!")

        val = self.items[self.head]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1

        self._downsize()

        return val


if __name__ == "__main__":
    random.seed(0)
    items = random.sample(list(range(1000)), 10)
    print(' '.join([str(x) for x in items]))
    print('\n')
    # queue = QueueLL()
    queue = QueueArr()
    for item in items:
        queue.enqueue(item)
        print(queue.items, queue.head, queue.tail)
    print(queue.get_print_string() + '\n')

    for _ in range(8):
        print(queue.dequeue())
        print(queue.items, queue.head, queue.tail)
    print('\n')
    print(queue.get_print_string() + '\n')

    for _ in range(2):
        print(queue.dequeue())
        print(queue.items, queue.head, queue.tail)
    print('\n')
    print(queue.get_print_string() + '\n')