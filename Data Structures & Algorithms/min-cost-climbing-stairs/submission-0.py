class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1]*len(cost)

        def dfs(idx):
            if idx >= len(cost):
                return 0
            if cache[idx] != -1:
                return cache[idx]

            cache[idx] = cost[idx]+min(dfs(idx+1), dfs(idx+2))
            return cache[idx]

        return min(dfs(0), dfs(1))