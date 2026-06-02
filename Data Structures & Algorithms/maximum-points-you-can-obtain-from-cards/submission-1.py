class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        l = 0
        r = len(cardPoints) - 1
        rIdx = len(cardPoints) - 1
        lsum = rsum = 0
        max_sum = 0

        for i in range(l, k):
            lsum += cardPoints[i]    
        max_sum = lsum

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rIdx]
            rIdx -= 1 
            max_sum = max(max_sum, lsum+rsum)

        return max_sum
