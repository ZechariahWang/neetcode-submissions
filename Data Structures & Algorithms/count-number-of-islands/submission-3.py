class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach: use dfs, explore all nodes
        # make an island_count var 
        # explore all neighbour nodes
        # if the current value explored value is larger or less than the boundaries, also return
        # if its a 1, its a valid
        # during this run, keep going while neightbours are also 1, as this is one island group, mark each node visited as 2 so we know we've been here already
        # if its a 0 or 2, we are at an edge, stop exploring in that direction
        # run dfs on every node, each time if the dfs run is valid, increase island_count by 1
        # after looping through every node, return island_count
        # time complexity: O(m*n) space: O(m*n)

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if grid[r][c] == "0" or grid[r][c] == "2":
                return 0
                
            grid[r][c] = "2"

            dfs(r+1, c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        island_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island_count += 1

        return island_count