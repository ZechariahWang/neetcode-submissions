class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach: use dfs
        # brute force check every grid, if its 1, then start a dfs search
        # go up down left right, if its a 1 then keep running dfs in that direction
        # for each tile u visit, mark it as visited by changing it from 1 to 2
        # after each successful dfs run once it completely exits out the dfs recursive loop, increase the count of islands by 1
        # at the very end, return the count of islands

        num_islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 

            if grid[r][c] == "2" or grid[r][c] == "0":
                return 

            grid[r][c] = "2"

            dfs(r+1, c)
            dfs(r, c+1) 
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(ROWS):
            for c  in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1

        return num_islands
