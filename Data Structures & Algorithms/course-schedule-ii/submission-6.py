class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for v, u in prerequisites:
            graph[u].append(v)
            
        state = [0]*numCourses #0->unvisited, 1->currently in path, 2->safe
        res = []

        def dfs(node):
            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            state[node] = 2
            res.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []

        res.reverse()
        return res