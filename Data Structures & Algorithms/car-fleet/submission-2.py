class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        cars = sorted([(p, (target-p) / s) for p,s in zip(position, speed)])

        res = 1
        _, prev = cars.pop()

        while cars:
            _, nxt = cars.pop()
            if nxt > prev:
                res += 1
                prev = nxt

        return res 