class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        pacific, atlantic = set(), set()

        def dfs(r,c,visited):
            visited.add((r,c))

            for i,j in moves:
                nr, nc = r+i, c+j
                if 0<=nr<rows and 0<=nc<cols:
                    if (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        #pacific
        for r in range(rows):
            dfs(r,0,pacific)

        for c in range(cols):
            dfs(0,c,pacific)

        #atlantic
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        
        for c in range(cols):
            dfs(rows-1,c,atlantic)

        #result
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res