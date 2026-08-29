from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        path = set()

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()
            res.append(node)

            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return [] if len(res) != numCourses else res