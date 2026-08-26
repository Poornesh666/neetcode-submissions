class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = ""

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        m, n = len(board), len(board[0])

        #storing in TrieNode
        for word in words:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isEnd = True
            curr.word = word

        def backtrack(i, j, node):
            if i<0 or i>=m or j<0 or j>=n or board[i][j] not in node.children:
                return

            next_node = node.children[board[i][j]]
            #mark
            ch = board[i][j]
            board[i][j] = "."

            if next_node.isEnd:
                res.append(next_node.word)
                next_node.isEnd = False

            #backtrack
            for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                r, c = i+i_off, j+j_off
                backtrack(r, c, next_node)
                    

            #unmark
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                backtrack(i, j, self.root)

        return res