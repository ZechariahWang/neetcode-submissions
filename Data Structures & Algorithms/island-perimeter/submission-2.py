class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # 2 = visited
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            elif grid[r][c] == 2:
                return 0

            grid[r][c] = 2
            perim = dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1)+ dfs(r-1, c)

            return perim

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r, c)

        return 0

        