class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = [False] * len(nums)

        def backtrack():
            #Base Condition
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i, num in enumerate(nums):
                if visited[i]:
                    continue

                visited[i] = True
                path.append(num)
                backtrack()
                path.pop()
                visited[i] = False

        backtrack()
        return res