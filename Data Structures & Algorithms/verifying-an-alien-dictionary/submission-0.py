class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        rank = defaultdict(int)

        for i, c in enumerate(order):
            rank[c] = i

        def invalid(w1, w2):

            for i in range(min(len(w1), len(w2))):

                if w1[i] != w2[i]:

                    if rank[w1[i]] > rank[w2[i]]:
                        return True

                    return False

            # All characters matched
            if len(w1) > len(w2):
                return True

            return False

        for i in range(len(words) - 1):

            if invalid(words[i], words[i + 1]):
                return False

        return True