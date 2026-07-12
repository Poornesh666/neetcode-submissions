class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = tank = 0
        n = len(gas)

        if sum(gas) - sum(cost) < 0: return -1

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start