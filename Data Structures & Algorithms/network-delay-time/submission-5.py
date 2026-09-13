class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        distance = [float('inf')]*(n+1)

        for u,v,cost in times:
            graph[u].append((v,cost)) 

        heap = [(0,k)] #distance, node
        distance[k] = 0

        while heap:
            dist, node = heapq.heappop(heap)
            
            for neighbor, d in graph[node]:
                new_dist = dist+d
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        res = max(distance[1:])
        return -1 if res == float('inf') else res