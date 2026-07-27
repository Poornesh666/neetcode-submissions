class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point
        for (x2, y2) in self.points:
            if x1 == x2 or y1 == y2 or abs(x1-x2) != abs(y1-y2):
                continue
            count += self.points[(x1,y2)] * self.points[(x2,y1)] * self.points[(x2, y2)]

        return count
        
