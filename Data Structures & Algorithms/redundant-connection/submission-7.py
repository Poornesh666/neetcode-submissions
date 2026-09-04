class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1

        def dfs(node, target, visited):
            if node == target:
                return True #cycle found
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True

            return False
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            if dfs(u,v,set()):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)