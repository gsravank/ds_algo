import random
import os


class BiNode:
    def __init__(self, val, prev_ptr=None, next_ptr=None):
        self.val = val
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr


class DequeueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        return

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def add_first(self, val):
        new_node = BiNode(val, self.head, None)
        if self.head is not None:
            self.head.next_ptr = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.count += 1
        return

    def add_last(self, val):
        new_node = BiNode(val, None, self.tail)
        if self.tail is not None:
            self.tail.prev_ptr = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.count += 1
        return

    def remove_first(self):
        if self.is_empty():
            raise Exception("Removing from an empty deck!")

        obj = self.head
        self.head = obj.prev_ptr
        self.count -= 1
        if self.head is None:
            self.tail = None
        else:
            self.head.next_ptr = None
        return obj.val

    def remove_last(self):
        if self.is_empty():
            raise Exception("Removing from an empty deck!")

        obj = self.tail
        self.tail = obj.next_ptr
        self.count -= 1
        if self.tail is None:
            self.head = None
        else:
            self.tail.prev_ptr = None
        return obj.val

    def iterator(self):
        obj = self.DeckIterator(self.tail)
        return obj

    class DeckIterator:
        def __init__(self, tail):
            self.curr_ptr = tail
            return

        def has_next(self):
            return self.curr_ptr is not None

        def next(self):
            if not self.has_next():
                raise Exception("Iterating after fully completing the deck!")

            val = self.curr_ptr.val
            self.curr_ptr = self.curr_ptr.next_ptr
            return val


if __name__ == "__main__":
    rand_numbers = sorted(random.sample(list(range(10000)), 10))
    print(' '.join([str(x) for x in rand_numbers]))

    deck = DequeueLL()

    for idx, number in enumerate(rand_numbers):
        if idx % 2 == 0:
            deck.add_first(number)
        else:
            deck.add_last(number)

    iter_obj = deck.iterator()
    print_things = list()
    while iter_obj.has_next():
        print_things.append(str(iter_obj.next()))
    print(' <=> '.join(print_things))

    print_things = list()
    for _ in range(10):
        val = deck.remove_last()
        print_things.append(str(val))
    print(' - '.join(print_things))
