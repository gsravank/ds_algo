"""
Give an algorithm to reverse the direction of a given singly linked list. In
other words, after the reversal all pointers should now point backwards. Your
algorithm should take linear time.
"""

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def create_ll_from_array(items):
    curr_node = None
    for idx in range(len(items) - 1, -1, -1):
        curr_node = Node(items[idx], curr_node)

    return curr_node


def print_ll(head, sep=' '):
    curr = head
    while curr is not None:
        print(curr.val, end=sep)
        curr = curr.next

    return


def reverse_ll(head):
    rev = None
    curr = head

    while curr is not None:
        curr_next = curr.next
        curr.next = rev
        rev = curr
        curr = curr_next

    return rev


numbers = list(range(1, 11))
ll = create_ll_from_array(numbers)
print_ll(ll, '->')
print('\n')

ll = reverse_ll(ll)
print_ll(ll, '->')
print('\n')


