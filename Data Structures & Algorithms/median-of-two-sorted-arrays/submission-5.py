class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A 

        total_len = len(nums1) + len(nums2)
        half = total_len // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l+r) // 2
            j = half - i - 2

            l1 = A[i] if i>=0 else float("-inf")
            l2 = B[j] if j>=0 else float("-inf")
            r1 = A[i+1] if (i+1) < len(A) else float("inf")
            r2 = B[j+1] if (j+1) < len(B) else float("inf")

            if l1 <= r2 and l2 <= r1:
                if total_len % 2:
                    return min(r1, r2)
                else:
                    return (min(r1,r2) + max(l1, l2)) / 2
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1