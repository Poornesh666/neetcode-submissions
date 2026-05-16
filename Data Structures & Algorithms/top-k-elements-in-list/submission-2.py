class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}

        for num in nums:
            temp[num] = temp.get(num, 0) + 1

        temp = (sorted(temp.items(), key = lambda x: x[1], reverse = True))

        return [k for k, v in temp[:k]]
        