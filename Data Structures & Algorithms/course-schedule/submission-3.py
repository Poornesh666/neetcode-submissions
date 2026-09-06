class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for v,u in prerequisites:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1

        q = deque() #courses
        #couses with indegree = 0
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return len(res) == numCourses