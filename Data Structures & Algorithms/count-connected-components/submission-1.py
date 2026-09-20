class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        components = n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]
        
        def union(n1, n2):
            nonlocal components
            root1, root2 = find(n1), find(n2)

            if root1 != root2:
                parent[root2] = root1
                components -= 1

        for u,v in edges:
            union(u,v)

        return components