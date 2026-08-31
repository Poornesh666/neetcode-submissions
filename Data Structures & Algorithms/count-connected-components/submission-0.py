class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
                 
        return res