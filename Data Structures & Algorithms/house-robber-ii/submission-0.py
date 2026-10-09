class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def solve(start, end):
            cache = [-1]*n
            def dfs(idx):
                if idx > end:
                    return 0
                if cache[idx] != -1:
                    return cache[idx]

                take = nums[idx]+dfs(idx+2)
                skip = dfs(idx+1)
                
                cache[idx] = max(take, skip)
                return cache[idx]
            
            return dfs(start)

        return max(solve(0, n-2), solve(1, n-1))