"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {} #og->clone
        def clone(node):
            if node is None:
                return None

            if node in hashmap:
               return hashmap[node]

            copy = Node(node.val)

            hashmap[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append(clone(neighbour))

            return copy

        return clone(node)