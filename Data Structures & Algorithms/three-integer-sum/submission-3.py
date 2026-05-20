class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            curr = nums[i]
            st = i+1
            end = len(nums) - 1
            while st < end:
                if nums[st] + nums[end] + curr == 0:
                    res.append([curr, nums[st], nums[end]])
                    st += 1
                    end -= 1
                    
                    while st < end and nums[st] == nums[st-1]:
                        st += 1
                    while st < end and nums[end] == nums[end+1]:
                        end -= 1

                elif nums[st] + nums[end] + curr < 0:
                    st += 1
                else:
                    end -= 1
                if nums[st] == nums[st-1]:
                    continue
            

        return res
