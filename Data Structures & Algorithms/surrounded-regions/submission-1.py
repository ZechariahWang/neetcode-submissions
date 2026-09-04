class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # approach: run dfs
        # explore every tile on the edge of the graph first, since these are definitely going to be safe
        # if one is found on the edge as a O, mark it as safe with a T, and run dfs off of that T node
        # From that T node, mark every connected O node as T as well to make it safe
        # outside the dfs loop, loop through every r and c and check if its on the edge
        # only if the the tile at that point is on an edge do u run dfs on it
        # afterwards loop through every tile again, and turn all T into O and turn all O into X

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

        