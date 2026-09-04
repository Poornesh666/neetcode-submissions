class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
                
        graph = [[] for _ in range(n)]
        degree = [0]*n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()
        for node in range(1, n):
            if degree[node] == 1:
                q.append(node)

        while q:
            node = q.popleft()
            degree[node] -= 1

            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    q.append(neighbor)

        cycle_nodes = set()
        for node in range(1, n):
            if degree[node] > 1:
                cycle_nodes.add(node)

        ans = []
        for u,v in edges:
            if u in cycle_nodes and v in cycle_nodes:
                ans = [u,v]

        return ans