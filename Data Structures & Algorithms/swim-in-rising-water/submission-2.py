class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        target = (n-1,n-1)
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        heap = [(grid[0][0],0,0)] #height, row, col
        visited = set()
        visited.add((0,0))

        while heap:
            height, row, col = heapq.heappop(heap)
            if (row, col) == target:
                return height
            
            for i, j in moves:
                nr, nc = row+i, col+j
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    maxi = max(height, grid[nr][nc])
                    heapq.heappush(heap,(maxi, nr, nc))
                # continue