import heapq

class Solution:
    def calculate(self, point):
        return point[0] * point[0] + point[1] * point[1]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            d = self.calculate(point)

            heapq.heappush(heap, (-d, point))

            if len(heap) > k:
                heapq.heappop(heap)


        return [point for _,point in heap]