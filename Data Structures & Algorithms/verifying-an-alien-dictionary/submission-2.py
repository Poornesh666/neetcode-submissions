class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c:i for i,c in enumerate(order)}

        def verified(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if index[w1[i]] < index[w2[i]]:
                    return True
                elif index[w1[i]] > index[w2[i]]:
                    return False

            return len(w1) <= len(w2)

        for i in range(len(words)-1):
            if not verified(words[i], words[i+1]):
                return False

        return True