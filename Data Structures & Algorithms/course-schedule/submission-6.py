class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for v,u in prerequisites:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1

        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        count = 0
        path = []
        while q:
            node = q.popleft()
            path.append(node)
            count += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses