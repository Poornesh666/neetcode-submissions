class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_map = []
        
        i,j = 0,0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_map.append(nums1[i])
                i += 1
            else:
                new_map.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            new_map.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            new_map.append(nums2[j])
            j += 1

        if len(new_map) % 2 == 0:
            idx1 = len(new_map) // 2
            idx2 = idx1 - 1
            return (new_map[idx1] + new_map[idx2]) / 2

        return new_map[len(new_map) // 2]