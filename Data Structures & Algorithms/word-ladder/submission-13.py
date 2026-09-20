class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0

        if beginWord in wordset:
            wordset.remove(beginWord)

        q = deque([(beginWord,1)]) #word, depth

        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordset:
                        q.append((newWord, depth+1))
                        wordset.remove(newWord)
        
        return 0