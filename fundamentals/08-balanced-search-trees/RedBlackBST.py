import random
import os


RED = True
BLACK = False


class Node:
    def __init__(self, key, val=None, color=False):
        self.key = key
        self.val = val
        self.color = color
        self.left = None
        self.right = None


def is_red(node):
    if node is None:
        return False
    return node.color == RED


class RedBlackBST:
    def __init__(self):
        self.root = None
        return

    def search(self, key):
        curr = self.root

        while curr is not None:
            if curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

        return None

    @staticmethod
    def _rotate_left(node):
        assert is_red(node.right)
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED

        return x

    @staticmethod
    def _rotate_right(node):
        assert is_red(node.left)
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        return x

    @staticmethod
    def _flip_colors(node):
        assert not is_red(node)
        assert is_red(node.left)
        assert is_red(node.right)
        node.left.color = BLACK
        node.right.color = BLACK
        node.color = RED
        return

    def _insert(self, node, key, val):
        if node is None:
            return Node(key, val, RED)

        if node.key < key:
            node.right = self._insert(node.right, key, val)
        elif node.key > key:
            node.left = self._insert(node.left, key, val)
        else:
            node.val = val

        if is_red(node.right) and not is_red(node.left):
            node = RedBlackBST._rotate_left(node)
        if is_red(node.left) and is_red(node.left.left):
            node = RedBlackBST._rotate_right(node)
        if is_red(node.left) and is_red(node.right):
            RedBlackBST._flip_colors(node)

        return node

    def insert(self, key, val=None):
        self.root = self._insert(self.root, key, val)
        self.root.color = BLACK
        return

    def print(self):
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.key
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s' % root.key
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + ('//' if is_red(root.left) else '/') + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s' % root.key
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s' % root.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + ('//' if is_red(root.left) else '/') + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        if self.root is None:
            return

        lines, *_ = display(self.root)
        for line in lines:
            print(line)
        return


if __name__ == "__main__":
    bst = RedBlackBST()
    # items = sorted(random.sample(list(range(100)), 31))
    items = random.sample(list(range(100)), 31)

    for idx in range(len(items)):
        item = items[idx]
        _ = os.system('clear')
        bst.print()
        print(f"Items so far: {' '.join([str(x) for x in items[:idx]])}")
        print(f"Current item: {items[idx]}")
        print(f"Next items: {' '.join([str(x) for x in items[idx + 1:]])}")
        bst.insert(item)
        bst.print()
        input()

    # bst.print()
