class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        stack = [] #store (position, time)

        for i in range(n):
            time = (target - position[i]) / speed[i]
            stack.append((position[i], time))

        res = 1
        stack = sorted(stack)
        _, prev = stack.pop()

        while stack:
            _, nxt = stack.pop()
            if nxt > prev:
                res += 1
                prev = nxt

        return res