class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for i, num in enumerate(nums):
            idxMap[num] = i

        for i, num in enumerate(nums):
            diff = target - num 
            if diff in idxMap and idxMap[diff] != i:
                return [i, idxMap[diff]]