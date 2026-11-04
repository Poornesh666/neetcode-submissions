class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i, val in enumerate(nums):
            # out of index from front
            if q and q[0] < i-k+1:
                q.popleft()

            # smaller elements from back
            while q and nums[q[-1]] < val:
                q.pop()

            # add index
            q.append(i)

            if i >= k-1:
                res.append(nums[q[0]])

        return res