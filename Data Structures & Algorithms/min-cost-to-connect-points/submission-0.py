class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = set()
        heap = [(0,0)] #distance, point
        res = 0

        while heap:
            cost, point = heapq.heappop(heap)

            if point in visited:
                continue
            visited.add(point)
            
            res += cost

            x1, y1 = points[point]
            for next_point in range(n):
                if next_point in visited:
                    continue

                x2, y2 = points[next_point]
                distance = abs(x1-x2)+abs(y1-y2)

                heapq.heappush(heap, (distance, next_point))

        return res
