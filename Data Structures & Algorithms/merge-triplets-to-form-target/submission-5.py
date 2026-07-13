class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for ls in triplets:
            if any(ls[i] > target[i] for i in range(3)): continue
            if ls[0] == target[0]: good.add(ls[0])
            if ls[1] == target[1]: good.add(ls[1])
            if ls[2] == target[2]: good.add(ls[2])

        return set(target) == good