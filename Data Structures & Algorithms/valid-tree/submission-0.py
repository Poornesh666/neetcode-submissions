class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(0)
        return len(visited) == n