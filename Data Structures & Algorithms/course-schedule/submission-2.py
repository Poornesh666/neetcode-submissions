class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        visited = set()
        count = 0
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()
            count += 1

            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return count == numCourses    