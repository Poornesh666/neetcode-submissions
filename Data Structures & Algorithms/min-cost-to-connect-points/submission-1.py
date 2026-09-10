class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0,0)] #cost, point
        visited = set()
        total = 0

        while heap:
            cost, point = heapq.heappop(heap)

            if point in visited:
                continue
            visited.add(point)

            total += cost
            x1, y1 = points[point]
            for i in range(len(points)):
                x2, y2 = points[i]
                dist = abs(x1-x2)+abs(y1-y2)
                heapq.heappush(heap, (dist, i))

        return total