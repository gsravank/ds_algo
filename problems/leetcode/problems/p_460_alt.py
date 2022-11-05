"""
https://leetcode.com/problems/lfu-cache/
"""
from collections import defaultdict


def print_ll(head, sep=' '):
    curr = head.next
    while curr.value is not None:
        print(f"({curr.key},{curr.value},{curr.freq})", end=sep)
        curr = curr.next


def print_freq_map(given_map, sep=' '):
    print('{', end='')
    for key, dll in given_map.items():
        if dll.sentinel.next.key is not None:
            print(f'{key}: {dll.sentinel.next.key}, ', end='')
    print('}', end=sep)
    return


class Node:
    def __init__(self, key=None, value=None, freq=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = prev
        self.next = next

        return


class DLL:
    def __init__(self):
        self._size = 0
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        return

    def is_empty(self):
        return self._size == 0

    def append(self, node):
        # Add after sentinel node
        next_node = self.sentinel.next
        node.next = next_node
        next_node.prev = node
        self.sentinel.next = node
        node.prev = self.sentinel
        self._size += 1
        return

    def pop(self, node):
        if self._size == 0:
            return

        next_node = node.next
        node.prev.next = next_node
        next_node.prev = node.prev
        self._size -= 1

        return


class LFUCache:
    def __init__(self, capacity):
        self.node_map = dict()
        self.freq_map = defaultdict(DLL)
        self.capacity = capacity
        self.min_freq = 0
        return

    def _update(self, node):
        # Pop the node
        freq = node.freq
        self.freq_map[freq].pop(node)

        # Increase frequency and update min frequency
        node.freq += 1
        if self.min_freq == freq and self.freq_map[freq].is_empty():
            self.min_freq = node.freq

        # Add to new DLL
        self.freq_map[node.freq].append(node)
        return

    def get(self, key):
        if self.capacity == 0 or key not in self.node_map:
            return -1

        node = self.node_map[key]
        self._update(node)

        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update(node)
        else:
            new_node = Node(key, value, 1)

            if len(self.node_map) == self.capacity:
                # Remove last item from current min frequency
                to_remove_node = self.freq_map[self.min_freq].sentinel.prev
                self.freq_map[self.min_freq].pop(to_remove_node)
                self.node_map.pop(to_remove_node.key)

            # Add node to DLL and map
            self.freq_map[1].append(new_node)
            self.node_map[key] = new_node

            # Update min frequency
            self.min_freq = 1

        return


tcs1 = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
tcs2 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

output = list()
for tc1, tc2 in zip(tcs1, tcs2):
    print(tc1, tc2, end='\t\t')
    if tc1 == 'LFUCache':
        obj = LFUCache(tc2[0])
        output.append(None)
    elif tc1 == 'put':
        obj.put(tc2[0], tc2[1])
        output.append(None)
    else:
        val = obj.get(tc2[0])
        output.append(val)

    for key, dll in obj.freq_map.items():
        if not dll.is_empty():
            print(key, end=':')
            print_ll(dll.sentinel, '=')
            print(' ', end='')
    print('\t', end='')
    print_freq_map(obj.freq_map, ' ')
    print()

print(output)
