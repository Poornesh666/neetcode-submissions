class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float('inf')]*n
        distance[src] = 0

        for _ in range(k+1):
            temp = distance.copy()
            for u,v,w in flights:
                if distance[u] != float('inf'):
                    temp[v] = min(temp[v], distance[u]+w)
            distance = temp

        return -1 if distance[dst] == float('inf') else distance[dst]