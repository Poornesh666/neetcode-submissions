class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
    
        for u,v,cost in flights:
            graph[u].append((v,cost))

        minHeap = [(0, src, 0)] #cost, node, stops
        
        distance = [[float('inf')]*(k+2) for _ in range(n)] #distance[node][stops]
        distance[src][0] = 0

        while minHeap:
            currCost, node, stops = heapq.heappop(minHeap)
            if node == dst:
                return currCost

            if stops > k:
                continue
            
            for neighbor, cost in graph[node]:
                newCost = currCost+cost
                newStops = stops+1
                if newCost < distance[neighbor][newStops]:
                    distance[neighbor][newStops] = newCost
                    heapq.heappush(minHeap, (newCost, neighbor, newStops))
        
        return -1