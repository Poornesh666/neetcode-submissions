class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        if beginWord in wordSet:
            wordSet.remove(beginWord)

        q = deque([(beginWord, 1)]) #word, count

        while q:
            word, count = q.popleft()
            if word == endWord:
                return count

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordSet:
                        q.append((newWord, count+1))
                        wordSet.remove(newWord)

        return 0