class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            hash_set.add(num)

        for i in range(len(nums)+1):
            if i not in hash_set:
                return i
                