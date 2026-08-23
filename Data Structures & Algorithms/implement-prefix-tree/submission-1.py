class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if(curr.children[idx] is None):
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]

        return curr.isEnd        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        
        return True
        
        