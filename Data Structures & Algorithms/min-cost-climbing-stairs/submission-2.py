class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2, prev1 = 0, 0

        for i in range(n-1, -1, -1):
            curr = cost[i] + min(prev2, prev1)

            prev2 = prev1
            prev1 = curr

        return min(prev2, prev1)            