class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [0, 0]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr[0], arr[1] = i, j
    
        return arr
            
