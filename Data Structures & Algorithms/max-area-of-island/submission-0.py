class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        largest_island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if grid[r][c] == 2: # marked/already visited
                return 0

            if grid[r][c] == 0:
                return 0

            if grid[r][c] == 1:
                grid[r][c] = 2

            return 1 + dfs(r, c-1) + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1)


        for r in range(ROWS):
            for c in range(COLS):
                    area = dfs(r, c)
                    if area >= largest_island:
                        largest_island = area

        return largest_island

        
        