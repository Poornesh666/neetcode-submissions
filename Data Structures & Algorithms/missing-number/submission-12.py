class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        add = 0
        for num in nums:
            add += num

        for i in range(len(nums)+1):
            add -= i

        return abs(add)

