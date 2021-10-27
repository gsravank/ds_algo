import random


class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node

    def set_val(self, val):
        self.val = val

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_val(self):
        return self.val

    def get_next_node(self):
        return self.next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_print_string(self):
        tmp_head = self.head
        print_items = list()
        while tmp_head is not None:
            print_items.append(str(tmp_head.get_val()))
            tmp_head = tmp_head.get_next_node()
        return ' -> '.join(print_items + ['None'])

    def insert_at_head(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        self.count += 1

    def return_val_at_head(self):
        if self.head is None:
            return None
        else:
            return self.head.get_val()

    def delete_val_at_head(self):
        if self.head is None:
            raise Exception("Unable to remove from an empty list")
        else:
            curr_head = self.head
            self.head = self.head.get_next_node()
            self.count -= 1

            return curr_head


if __name__ == "__main__":
    items = random.sample(list(range(1000)), 30)
    ll = LinkedList()

    print(' '.join([str(x) for x in items]))
    print('\n')

    for item in items:
        ll.insert_at_head(item)

    print(ll.get_print_string())
    print('\n')

    for _ in range(10):
        ll.delete_val_at_head()

    print(ll.get_print_string())
    print('\n')

    for _ in range(19):
        ll.delete_val_at_head()
    print(ll.get_print_string())
    print('\n')

    for _ in range(1):
        ll.delete_val_at_head()
    print(ll.get_print_string())
    print('\n')
