class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        MOVES = [(0,1),(1,0),(0,-1),(-1,0)]

        visited = set()
        heap = [(0,0,0)] #effort, row, col

        while heap:
            effort, row, col = heapq.heappop(heap)
            
            if (row,col) == (ROWS-1, COLS-1):
                return effort

            if (row,col) in visited:
                continue

            visited.add((row,col))

            for i,j in MOVES:
                nr, nc = row+i, col+j
                if (0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited):
                    new_effort = max(effort, abs(heights[nr][nc]-heights[row][col]))
                    heapq.heappush(heap, (new_effort, nr, nc))

        return 0