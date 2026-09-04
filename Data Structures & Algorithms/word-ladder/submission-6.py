class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        if beginWord in wordSet:
            wordSet.remove(beginWord)

        q = deque([(beginWord, 1)]) #word, count
        
        def isValid(word1, word2):
            if len(word1) != len(word2):
                return False

            n,count = len(word1), 0
            for i in range(n):
                if word1[i] != word2[i]:
                    count += 1

            return count == 1

        while q:
            word, count = q.popleft()
            if word == endWord:
                return count

            for w in list(wordSet):
                if isValid(w, word):
                    q.append((w, count+1))
                    wordSet.remove(w)

        return 0