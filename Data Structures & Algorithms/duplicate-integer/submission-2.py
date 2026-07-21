class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set(nums)
        return len(hash_set) != len(nums)