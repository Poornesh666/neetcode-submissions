class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        
        while q:
            r,c = q.popleft()

            for i,j in moves:
                nr, nc = r+i, c+j
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))