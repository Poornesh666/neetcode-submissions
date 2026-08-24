class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.isEnd

            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(child, idx+1):
                        return True
                return False


            if word[idx] not in node.children:
                return False
            

            return dfs(node.children[word[idx]], idx+1)

        return dfs(self.root, 0)