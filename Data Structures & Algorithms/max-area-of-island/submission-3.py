class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # approach: run dfs
        # loop through all tiles, if a tile is == 1, then start a dfs run, in the dfs run, return 1 + dfs in all dir
        # in the dfs loop if the current tile is 1, return 1, else return 0
        # afterwards, mark the tile as 2 so that we know we visited it
        # outside, update a max_area var through each iteration

        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if grid[r][c] == 0 or grid[r][c] == 2:
                return 0

            grid[r][c] = 2

            return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area
        
        