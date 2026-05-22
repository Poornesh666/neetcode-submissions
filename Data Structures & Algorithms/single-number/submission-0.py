class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}

        for num in nums:
            temp[num] = temp.get(num,0) + 1

        for num, freq in temp.items():
            if freq == 1:
                return num        