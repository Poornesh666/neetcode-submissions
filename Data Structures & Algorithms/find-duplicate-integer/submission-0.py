class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = set()
        for num in nums:
            if num in freq:
                return num
            freq.add(num)