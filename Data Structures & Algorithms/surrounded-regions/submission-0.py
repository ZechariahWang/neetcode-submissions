class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # approach: run dfs
        # explore every possible tile in the grid
        # if its a 0, then mark it as a potential candidate
        # run dfs in all other 8 direction. If the grid is on an edge, it cant be surrounded so just ignore it
        # otherwise, if dfs is valid in all 8 directions, then this current 0 grid can be surrounded turn it into an X
        # modify the board list in place

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >=ROWS or c >= COLS or board[r][c] != "O":
                return 

            board[r][c]="T"
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if r== 0 or r == ROWS-1 or c == 0 or c==COLS-1:
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        