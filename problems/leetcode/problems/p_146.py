"""
https://leetcode.com/problems/lru-cache/
"""


class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

        return


def delete_node(node):
    prev_node = node.prev
    prev_node.next = node.next
    node.next.prev = prev_node
    return


def add_node_next_to(curr_node, new_node):
    next_node = curr_node.next
    curr_node.next = new_node
    new_node.prev = curr_node
    new_node.next = next_node
    next_node.prev = new_node
    return


def add_node_before(curr_node, new_node):
    prev_node = curr_node.prev
    new_node.next = curr_node
    curr_node.prev = new_node
    new_node.prev = prev_node
    prev_node.next = new_node
    return


def print_ll(head, sep=' '):
    curr = head.next
    while curr.val is not None:
        print(f"({curr.key}, {curr.val})", end=sep)
        curr = curr.next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # Hashmap from keys to nodes
        self.key_to_node = dict()

        # DLL
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        return

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        else:
            matching_node = self.key_to_node[key]
            delete_node(matching_node)
            # add_node_next_to(self.tail.prev, matching_node)
            add_node_before(self.tail, matching_node)
            return matching_node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            new_node = Node(key, value)

            # Remove head node
            if self.size == self.capacity:
                lru_node = self.head.next
                delete_node(lru_node)
                del self.key_to_node[lru_node.key]
            else:
                self.size += 1

            # Add new node before tail
            add_node_next_to(self.tail.prev, new_node)
            self.key_to_node[key] = new_node
        else:
            matching_node = self.key_to_node[key]
            delete_node(matching_node)
            # Change value
            matching_node.val = value
            # Add node before tail
            add_node_before(self.tail, matching_node)
            self.key_to_node[key] = matching_node
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

tcs1 = ["LRUCache","put","put","get","put","get","put","get","put", "put", "get"]
tcs2 = [[3],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3,10],[2,2],[3]]


output = list()
for tc1, tc2 in zip(tcs1, tcs2):
    print(tc1, tc2, end='\t\t')
    if tc1 == 'LRUCache':
        obj = LRUCache(tc2[0])
        output.append(None)
    elif tc1 == 'put':
        obj.put(tc2[0], tc2[1])
        output.append(None)
    else:
        val = obj.get(tc2[0])
        output.append(val)
    
    print_ll(obj.head, '=')
    print()

print(output)
