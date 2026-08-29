from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for v, u in prerequisites:
            graph[u].append(v)

        visited = set()
        path = set()
        count = 0

        def dfs(node):
            nonlocal count
            if node in path:
                return False
            
            if node in visited:
                return True

            path.add(node)

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            path.remove(node)
            visited.add(node)
            count += 1            
            return True

        for node in range(numCourses):
            if node not in visited:
                dfs(node)
                    
        return count == numCourses