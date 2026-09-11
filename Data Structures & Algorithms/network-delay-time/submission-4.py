class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,cost in times:
            graph[u].append((v,cost))

        distance = [float('inf')]*(n+1)
        distance[k] = 0

        heap = [(0,k)] #distance,source node

        while heap:
            curr_dist, node = heapq.heappop(heap)

            for neighbor, dist in graph[node]:
                new_dist = curr_dist+dist
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        res = max(distance[1:])
        return res if res != float('inf') else -1
