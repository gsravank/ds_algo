"""
https://leetcode.com/problems/lfu-cache/
"""
import math


class Node:
    def __init__(self, key=None, val=None, prev=None, next=None, freq=0):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = freq
        return


def print_ll(head, sep=' '):
    curr = head.next
    while curr.val is not None:
        print(f"({curr.key},{curr.val},{curr.freq})", end=sep)
        curr = curr.next


def print_freq_map(given_map, sep=' '):
    print('{', end='')
    for key, node in given_map.items():
        print(f'{key}: {node.key}, ', end='')
    print('}', end=sep)
    return


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.freq_map = dict()
        self.node_map = dict()

        self.head = Node(freq=0)
        self.tail = Node(freq=math.inf)
        self.head.next = self.tail
        self.tail.prev = self.head
        return

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key not in self.node_map:
            return -1
        else:
            curr_node = self.node_map[key]
            prev_node = curr_node.prev
            next_node = curr_node.next

            if self.freq_map[curr_node.freq].next.freq == curr_node.freq + 1:
                if prev_node.freq == curr_node.freq:
                    self._remove(curr_node)
                    curr_node.freq += 1
                    self._add(self.freq_map[curr_node.freq], curr_node)
                    self.freq_map[curr_node.freq] = curr_node
                    if prev_node.next.freq != prev_node.freq:
                        self.freq_map[prev_node.freq] = prev_node
                else:
                    if next_node.freq == curr_node.freq:
                        # this is the first node in the bunch
                        self._remove(curr_node)
                        curr_node.freq += 1
                        self._add(self.freq_map[curr_node.freq], curr_node)
                        self.freq_map[curr_node.freq] = curr_node
                    else:
                        # This is the only node in the bunch
                        self._remove(curr_node)
                        curr_node.freq += 1
                        self._add(self.freq_map[curr_node.freq], curr_node)
                        self.freq_map[curr_node.freq] = curr_node

                        self.freq_map.pop(curr_node.freq - 1)
            else:
                curr_node.freq += 1
                if self.freq_map[curr_node.freq - 1] != curr_node:
                    self._remove(curr_node)
                    self._add(self.freq_map[curr_node.freq - 1], curr_node)
                    self.freq_map[curr_node.freq] = curr_node
                else:
                    self.freq_map[curr_node.freq] = curr_node

                if curr_node.prev.freq == curr_node.freq - 1:
                    self.freq_map[curr_node.freq - 1] = curr_node.prev
                else:
                    self.freq_map.pop(curr_node.freq - 1)

            return curr_node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None

        if key in self.node_map:
            curr_node = self.node_map[key]
            curr_node.val = value
            prev_node = curr_node.prev
            next_node = curr_node.next

            if self.freq_map[curr_node.freq].next.freq == curr_node.freq + 1:
                if prev_node.freq == curr_node.freq:
                    self._remove(curr_node)
                    curr_node.freq += 1
                    self._add(self.freq_map[curr_node.freq], curr_node)
                    self.freq_map[curr_node.freq] = curr_node
                    if prev_node.next.freq != prev_node.freq:
                        self.freq_map[prev_node.freq] = prev_node
                else:
                    if next_node.freq == curr_node.freq:
                        # this is the first node in the bunch
                        self._remove(curr_node)
                        curr_node.freq += 1
                        self._add(self.freq_map[curr_node.freq], curr_node)
                        self.freq_map[curr_node.freq] = curr_node
                    else:
                        # This is the only node in the bunch
                        self._remove(curr_node)
                        curr_node.freq += 1
                        self._add(self.freq_map[curr_node.freq], curr_node)
                        self.freq_map[curr_node.freq] = curr_node

                        self.freq_map.pop(curr_node.freq - 1)
            else:
                curr_node.freq += 1
                if self.freq_map[curr_node.freq - 1] != curr_node:
                    self._remove(curr_node)
                    self._add(self.freq_map[curr_node.freq - 1], curr_node)
                    self.freq_map[curr_node.freq] = curr_node
                else:
                    self.freq_map[curr_node.freq] = curr_node

                if curr_node.prev.freq == curr_node.freq - 1:
                    self.freq_map[curr_node.freq - 1] = curr_node.prev
                else:
                    self.freq_map.pop(curr_node.freq - 1)

            return curr_node.val
        else:
            new_node = Node(key, value, freq=1)
            if len(self.node_map) == self.capacity:
                to_remove_node = self.head.next
                to_remove_next = to_remove_node.next
                to_remove_freq = to_remove_node.freq

                if to_remove_node.freq == to_remove_next.freq:
                    self.node_map.pop(to_remove_node.key)
                    self._remove(to_remove_node)
                    self._add(self.freq_map.get(1, self.head), new_node)
                    self.freq_map[1] = new_node
                    self.node_map[key] = new_node
                else:
                    self._remove(to_remove_node)
                    self._add(self.head, new_node)
                    self.node_map.pop(to_remove_node.key)
                    self.freq_map.pop(to_remove_freq)
                    self.node_map[key] = new_node
                    self.freq_map[1] = new_node
            else:
                prev_node = self.freq_map.get(1, self.head)
                self._add(prev_node, new_node)
                self.freq_map[1] = new_node
                self.node_map[key] = new_node

        return

    def _remove(self, node):
        next_node = node.next
        node.prev.next = next_node
        next_node.prev = node.prev
        return

    def _add(self, curr_node, new_node):
        next_node = curr_node.next
        curr_node.next = new_node
        new_node.prev = curr_node
        new_node.next = next_node
        next_node.prev = new_node

        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


tcs1 = ["LFUCache","put","get"]
tcs2 = [[0], [0,0],[0]]

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

    print_ll(obj.head, '=')
    print('\t', end='')
    print_freq_map(obj.freq_map, ' ')
    print()

print(output)
