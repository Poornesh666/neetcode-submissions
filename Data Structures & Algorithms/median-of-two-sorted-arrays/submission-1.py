class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_map = []

        for num in nums1:
            new_map.append(num)
        
        for num in nums2:
            new_map.append(num)

        new_map.sort()

        if len(new_map) % 2 == 0:
            idx1 = int(len(new_map)/2) 
            idx2 = idx1 - 1
            res = (new_map[idx1] + new_map[idx2])/2 
        else:
            idx = int(math.floor(len(new_map)/2))
            res = new_map[idx]

        return res