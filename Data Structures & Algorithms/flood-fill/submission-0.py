class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        
        def dfs(r, c):
            original_col = image[r][c]

            if original_col == color:
                return

            image[r][c] = color

            for ri, cj in moves:
                nr, nc = r+ri, c+cj
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_col:
                    dfs(nr, nc)

        dfs(sr, sc)
        return image