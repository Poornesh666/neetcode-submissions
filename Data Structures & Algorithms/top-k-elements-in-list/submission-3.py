class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}

        for num in nums:
            temp[num] = temp.get(num, 0) + 1

        temp = dict(sorted(temp.items(), key = lambda x: x[1], reverse = True))

        return list(temp.keys())[:k]
        