class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            while heap and count[heap[0]] == 0:
                heapq.heappop(heap)

            if not heap:
                break

            card = heap[0]
            for i in range(card, card + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1

        return True