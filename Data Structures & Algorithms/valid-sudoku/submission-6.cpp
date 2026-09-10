class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // approach: 
        // we can map each 3x3 grid individually by dividing the current index by 3
        // if its equal to 0 (bc of integer math, it will correspond to the first grid ex: 1/3 = 0)
        // if its 3-5, then it corresponds to the second grid since 3/3=1
        // if its anything greater than 5 it corresponds to third grid since itll be equal to two, which is the second index
        // make a default dictionaryt with the default value being a list, do this for rows, cols, and each grid, each item in the default dict represents one of the corresponding items 
        // (ex one list represents one row)
        // loop through every r in the board
        // loop through every c in the board, the r and c correspond to a tile on the sudoku board
        // we want to check in groups of 3x3 to see if they are valid
        // if the current tile value == . just ignore and move onto next tile
        // if the current tile value is already inside a corresponding row, col, or grid, automatically invalid, return false
        // otherwise, keep going in the loop, this is still a valid board. append the value of the current grid to the corresponding list in the rows, cols, grid list

        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_map<int, unordered_set<char>>> grid;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') { continue; }
                if (rows[r].count(board[r][c]) || cols[c].count(board[r][c]) || grid[r/3][c/3].count(board[r][c])) { return false; }

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                grid[r/3][c/3].insert(board[r][c]);
            }
        }

        return true;

    }
};