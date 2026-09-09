class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        heap = [(0,0,0)] #effort, row, col
        visited = set()
        
        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r,c) == (rows-1,cols-1):
                return effort

            if (r,c) in visited:
                continue
            visited.add((r,c))

            for i,j in moves:
                nr, nc = r+i, c+j
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                    neffort = max(effort, abs(heights[r][c]-heights[nr][nc]))
                    heapq.heappush(heap, (neffort, nr, nc))

        return 0