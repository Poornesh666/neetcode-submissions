import heapq

class Solution:
    def calculate(self, point):
        return point[0] * point[0] + point[1] * point[1]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []

        for point in points:
            d = self.calculate(point)
            distance.append((-d, point))

        heapq.heapify(distance)

        while len(distance) > k:
            heapq.heappop(distance)

        return [point for _,point in distance]