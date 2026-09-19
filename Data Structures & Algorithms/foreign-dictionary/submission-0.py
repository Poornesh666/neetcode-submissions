class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = set()

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        indegree = {c:0 for c in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1 
            
        queue = deque()
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) != len(graph):
            return ""

        return "".join(res)