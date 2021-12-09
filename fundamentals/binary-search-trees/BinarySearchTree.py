from utils.DSUtils import print_tree
import os
import random


class Node:
    def __init__(self, key, val=None, left=None, right=None, properties=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if properties is None:
            self.properties = dict()
        else:
            self.properties = properties
        return

    def __str__(self):
        return f"[{self.key}, {self.val}]"


# Assume no duplicates
class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _insert_rec(node, key, val):
        if node is None:
            return Node(key, val)
        elif node.key < key:
            node.right = BinarySearchTree._insert_rec(node.right, key, val)
            return node
        elif node.key > key:
            node.left = BinarySearchTree._insert_rec(node.left, key, val)
            return node
        else:
            raise Exception(f"Key {key} already present! Don't insert duplicates")

    def insert_rec(self, key, val=None):
        self.root = BinarySearchTree._insert_rec(self.root, key, val)
        return

    def insert_iter(self, key, val=None):
        curr = self.root
        if curr is None:
            self.root = Node(key, val)
            return
        else:
            if curr.key == key:
                raise Exception(f"Key {key} already present! Don't insert duplicates")
            done = (curr.left is None and curr.right is None)
            while not done:
                if curr.key < key:
                    curr = curr.right
                elif curr.key > key:
                    curr = curr.left
                else:
                    raise Exception(f"Key {key} already present! Don't insert duplicates")

                done = (curr.left is None and curr.right is None)

            if curr.key < key:
                curr.right = Node(key, val)
            elif curr.key > key:
                curr.left = Node(key, val)
            else:
                raise Exception(f"Key {key} already present! Don't insert duplicates")
        return

    def search(self, key):
        curr = self.root
        while curr is not None:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr
        return None

    @staticmethod
    def minimum(curr):
        if curr is None:
            return None

        while curr.left is not None:
            curr = curr.left

        return curr

    @staticmethod
    def maximum(curr):
        if curr is None:
            return None

        while curr.right is not None:
            curr = curr.right

        return curr

    @staticmethod
    def _delete_minimum(node):
        if node is None:
            return None
        elif node.left is None:
            return node.right
        else:
            node.left = BinarySearchTree._delete_minimum(node.left)
            return node

    def delete_minimum(self):
        self.root = BinarySearchTree._delete_minimum(self.root)
        return

    @staticmethod
    def _delete_maximum(node):
        if node is None:
            return None
        elif node.right is None:
            return node.left
        else:
            node.right = BinarySearchTree._delete_maximum(node.right)
            return node

    def delete_maximum(self):
        self.root = BinarySearchTree._delete_maximum(self.root)
        return

    @staticmethod
    def _delete(node, k):
        if node is None:
            return None

        if node.key > k:
            node.left = BinarySearchTree._delete(node.left, k)
        elif node.key < k:
            node.right = BinarySearchTree._delete(node.right, k)
        else:
            # One child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Two children
            min_in_right = BinarySearchTree.minimum(node.right)
            node.key = min_in_right.key
            node.val = min_in_right.val
            node.right = BinarySearchTree._delete_minimum(node.right)
        return node

    def delete(self, key):
        self.root = BinarySearchTree._delete(self.root, key)
        return

    @staticmethod
    def _assign_heights(node):
        if node is None:
            return 0
        else:
            node.properties['height'] = 1 + max(BinarySearchTree._assign_heights(node.left), BinarySearchTree._assign_heights(node.right))

            return node.properties['height']

    def assign_heights(self):
        BinarySearchTree._assign_heights(self.root)
        return self.root.properties['height']


if __name__ == "__main__":
    bst = BinarySearchTree()
    items = list(range(32))
    random.shuffle(items)
    print(items)

    for idx, item in enumerate(items):
        bst.insert_rec(item)
        print(f"N = {idx + 1}\nHeight: {bst.assign_heights()}\n")
        print_tree(bst.root, 'key')
        input()
        os.system('clear')
        os.system("printf '\033c'")

    print_tree(bst.root, 'key')
    print(f"Height: {bst.assign_heights()}")

    minimum_node = BinarySearchTree.minimum(bst.root)
    maximum_node = BinarySearchTree.maximum(bst.root)
    print(f"Minimum: {minimum_node.key}")
    print(f"Maximum: {maximum_node.key}\n")

    bst.delete_minimum()
    print_tree(bst.root, 'key')
    print(f"Height: {bst.assign_heights()}")

    minimum_node = BinarySearchTree.minimum(bst.root)
    maximum_node = BinarySearchTree.maximum(bst.root)
    print(f"Minimum: {minimum_node.key}")
    print(f"Maximum: {maximum_node.key}\n")

    bst.delete_maximum()
    print_tree(bst.root, 'key')
    print(f"Height: {bst.assign_heights()}")

    minimum_node = BinarySearchTree.minimum(bst.root)
    maximum_node = BinarySearchTree.maximum(bst.root)
    print(f"Minimum: {minimum_node.key}")
    print(f"Maximum: {maximum_node.key}\n")
