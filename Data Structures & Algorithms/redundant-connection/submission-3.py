class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges)+1)]
        degree = [0]*(len(edges)+1)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque()
        for node in range(1, len(edges)+1):
            if degree[node] == 1:
                q.append(node)

        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    q.append(neighbor)

        cycle_nodes = set()
        for node in range(1, len(edges)+1):
            if degree[node] > 1:
                cycle_nodes.add(node)

        ans = []
        for u, v in edges:
            if u in cycle_nodes and v in cycle_nodes:
                ans = [u,v]

        return ans