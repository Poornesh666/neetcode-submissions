class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        count = 0
        res = []
        while q:
            node = q.popleft()
            count += 1
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return [] if count != numCourses else res