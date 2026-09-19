class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        def union(n1, n2):
            parent[n2] = n1

        for u,v in edges:
            root1, root2 = find(u), find(v)
            if root1 != root2:
                union(root1,root2)

            if root1 == root2:
                return [u,v]