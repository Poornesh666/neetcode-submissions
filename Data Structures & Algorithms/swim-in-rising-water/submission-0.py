class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        visited = set()
        heap = [(grid[0][0], 0, 0)] #height, r, c
        visited.add((0,0))
        
        while heap:
            height, r, c = heapq.heappop(heap)
            if (r,c) == (n-1, n-1):
                return height

            for i,j in moves:
                nr, nc = r+i, c+j
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(heap, (max(grid[nr][nc], height), nr, nc))
                continue