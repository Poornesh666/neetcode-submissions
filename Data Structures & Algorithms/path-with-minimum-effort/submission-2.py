class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        MOVES = [(0,1),(1,0),(0,-1),(-1,0)]

        heap = [(0,0,0)] #moves, row, col

        distance = [[float('inf')]*COLS 
                    for _ in range(ROWS)]
        distance[0][0] = 0

        while heap:
            curr_effort, row, col = heapq.heappop(heap)

            if (row, col) == (ROWS-1, COLS-1):
                return curr_effort

            if curr_effort > distance[row][col]:
                continue

            for i,j in MOVES:
                nr, nc = row+i, col+j
                if 0<=nr<ROWS and 0<=nc<COLS:
                    new_effort = max(curr_effort, abs(heights[nr][nc] - heights[row][col]))
                    if new_effort < distance[nr][nc]:
                        distance[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0
