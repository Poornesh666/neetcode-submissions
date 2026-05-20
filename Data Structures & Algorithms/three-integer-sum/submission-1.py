class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            curr = nums[i]
            st = i+1
            end = len(nums) - 1
            while st < end:
                if nums[st] + nums[end] + curr == 0:
                    res.add((curr, nums[st], nums[end]))
                    st += 1
                    end -= 1
                elif nums[st] + nums[end] + curr < 0:
                    st += 1
                else:
                    end -= 1

        return list(res)
