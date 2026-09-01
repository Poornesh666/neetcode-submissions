class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        row, col = len(grid), len(grid[0])
        time, fresh = 0, 0

        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for i,j in moves:
                    nr, nc = r+i, c+j
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time += 1
        
        return time if not fresh else -1