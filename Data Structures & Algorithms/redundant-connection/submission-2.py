class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges)+1)]
        indegree = [0]*(len(edges)+1)

        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
            graph[v].append(u)
            indegree[u] += 1

        q = deque()
        for node in range(1, len(edges)+1):
            if indegree[node] == 1:
                q.append(node)

        while q:
            node = q.popleft()
            indegree[node] -= 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    q.append(neighbor)

        for u,v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u,v]

        return []
