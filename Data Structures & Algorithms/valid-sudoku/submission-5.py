class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach:
        # isntead of checking if valid, check if its NOT valid
        # three conditions: loop through every single grid since we know its 9x9
        #
        #
        # declare a default dict with the default val as a set for rows, cols, and the board
        # loop through all the rows
        # loop through all the columns
        # check if the current grid is in the current row and its in the current col or the current grid (3x3)
        # if its already in there, then u know theres a duplicate, therefore its not valid
        # otherwise, its valid so far so keep going
        # once you reach the end, return true

        ROWS = len(board)
        COLS = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(r//3, c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3, c//3)].add(board[r][c])

        return True
