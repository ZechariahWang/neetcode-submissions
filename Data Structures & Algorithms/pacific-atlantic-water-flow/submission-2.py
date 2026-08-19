class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # approach: use dfs
        # make a visited set
        # loop through every grid, and then check the neighboring nodes values
        # add node to visited set
        # if they are <= the current node val, they are still valid so continue
        # else, if the neighbor node is greater than the current node val, stop exploring as it definitely not valid
        # continue this loop until its able to find one node that branches out into either the top left side AND another node the bottom and right side
        # if r < 0 or c < 0, then it went into the pacific, if r>= len(ROWS) or c>= len(COLS), its in the atlantic
        # Once you are able to satisfy this, then that means u have a valid path, therefore this node is valid
        # return hit_pacific=True, hit_atlantic=True inside the DFS call
        # outside the dfs loop, loop through every r in rows
        # inside that loop, loop through every c in cols
        # if dfs(r,c, hit_pacific, hit_atlantic) is valid, stores its [r, c] values, append it to res list
        # outside the two loops, return res

        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        pac, atl = set(), set()

        def dfs(r, c, prev_height, visit_set):
            if r < 0 or c < 0:
                return
            if r >= ROWS or c >= COLS:
                return
            if (r, c) in visit_set:
                return
            if heights[r][c] < prev_height:
                return 

            visit_set.add((r, c))
            dfs(r+1,c, heights[r][c], visit_set)
            dfs(r,c+1, heights[r][c], visit_set)
            dfs(r-1,c, heights[r][c], visit_set)
            dfs(r,c-1, heights[r][c], visit_set)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS-1, heights[r][COLS-1], atl)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)

        return [[r,c] for r, c in pac & atl]

        