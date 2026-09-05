class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        if beginWord in wordSet:
            wordSet.remove(beginWord)

        q = deque([(beginWord,1)]) #word, depth

        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordSet:
                        q.append((newWord, depth+1))
                        wordSet.remove(newWord)

        return 0
                        
            