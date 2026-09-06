class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n+1)]

        for u,v,time in times:
            graph[u].append((v,time))

        dist = [float('inf')]*(n+1)
        dist[k] = 0

        minHeap = [(0,k)] #weight, node

        while minHeap:
            currentWeight, node = heapq.heappop(minHeap)

            for neighbor, weight in graph[node]:
                newDist = weight+currentWeight
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    heapq.heappush(minHeap, (newDist, neighbor))

        maxDist = max(dist[1:])
        return -1 if maxDist == float('inf') else maxDist