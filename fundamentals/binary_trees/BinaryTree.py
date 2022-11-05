import random

random.seed(0)

class Node:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

        return


def _create_binary_tree(root, numbers):
    n = len(numbers)
    idx = random.randint(0, n-1)
    # idx = n // 2

    root.val = numbers[idx]

    if idx == n-1:
        root.right = None
    else:
        right = Node()
        root.right = _create_binary_tree(right, numbers[idx + 1:])
        right.parent = root

    if idx == 0:
        root.left = None
    else:
        left = Node()
        root.left = _create_binary_tree(left, numbers[:idx])
        left.parent = root

    return root


def create_binary_tree(numbers):
    root = Node()
    root = _create_binary_tree(root, numbers)
    return root


def pre_order_traversal(root, sep=' '):
    if root is None:
        return

    print(root.val, end=sep)
    pre_order_traversal(root.left, sep)
    pre_order_traversal(root.right, sep)

    return


def post_order_traversal(root, sep=' '):
    if root is None:
        return

    post_order_traversal(root.left, sep)
    post_order_traversal(root.right, sep)
    print(root.val, end=sep)

    return


def in_order_traversal(root, sep=' '):
    if root is None:
        return

    in_order_traversal(root.left, sep)
    print(root.val, end=sep)
    in_order_traversal(root.right, sep)

    return


def in_order_traversal_iter(root, sep=' '):
    def travel_up(node):
        curr_node = node
        done = (node == root) or (node == node.parent.left)
        while not done:
            # print(f"TUF: {curr_node.val}")
            done = (curr_node == root) or (curr_node == curr_node.parent.left)
            if not done:
                curr_node = curr_node.parent
        return curr_node

    def travel_down(node):
        curr_node = node
        while curr_node is not None and curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node
    
    # Try using a sentinel
    # Go left most child and add dummy node to its left? Or keep the entire tree to the left of a dummy node
    # Start post order traversal from this dummy node?
    # Add sentinels to every leaf node (to both left and right)
    sentinel = Node(None, root)
    currNode = sentinel
    
    done = False
    while not done:
        currNode = travel_down(currNode)
        # print(f"TD: {currNode.val}")
        if currNode.right is None:
            if currNode.val:
                print(currNode.val, end=sep)
            currNode = travel_up(currNode)
            if currNode == root:
                return
            elif currNode.parent.right is None:
                # Adding a sentinel node to be able to travel up again from here
                currNode.parent.right = Node(parent=currNode.parent)
                # Alternatively keep travelling up till you find a parent with a valid right child
                # or till the root

            print(currNode.parent.val, end=sep)  # Printing root
            currNode = currNode.parent.right  # Go to right subtree of root and restart process
        else:
            # Case of both left and right children are None
            if currNode.val:
                print(currNode.val, end=sep)
            currNode = currNode.right
    
    return


numbers = list(range(1, 32))
root = create_binary_tree(numbers)

in_order_traversal(root)
print()
# pre_order_traversal(root)
# print()
post_order_traversal(root)
print()


print()
in_order_traversal_iter(root)
