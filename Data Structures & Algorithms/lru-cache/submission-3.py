class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        pre = node.prev
        nxt = node.next

        pre.next = nxt
        nxt.prev = pre

    def insert(self, node):
        pre = self.right.prev
        nxt = self.right

        pre.next = node
        nxt.prev = node
        node.prev = pre
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        else:
            old_node = self.cache[key]
            old_node.value = value
            self.remove(old_node)
            self.insert(old_node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        