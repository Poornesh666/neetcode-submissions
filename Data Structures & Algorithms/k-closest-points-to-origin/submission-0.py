import math

class Solution:
    def calculate(self, point: List[int]):
            return math.sqrt(((point[0] - 0) * (point[0] - 0))+(point[1] - 0) * (point[1] - 0))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = []
        for point in points:
            distance.append((self.calculate(point), point))

        distance.sort()

        return [point for _, point in distance[:k]]

        