class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        choice = []
        visited = [False]*len(nums) 
        def backtrack():
            # base condition
            if len(choice) == len(nums):
                res.append(choice.copy())
                return

            # adding into choice
            for i, num in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                choice.append(num)
                backtrack()
                choice.pop()
                visited[i] = False

        backtrack()
        return res