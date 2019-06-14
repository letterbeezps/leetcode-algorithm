class Solution {
    public void solveSudoku(char[][] board) {
        if (board == null || board.length != 9 || board[0].length != 9) return;
        boolean tmp = solveSudokuHelper(board, 0, 0);
    }
    
    public boolean solveSudokuHelper(char[][] board, int row, int col) {
        if (board == null || board.length != 9 || board[0].length != 9) return false;
        
        while (row < 9 && col < 9) {
            if (board[row][col] == '.') break; //find the empty cell
            if (col == 8) {
                col = 0;
                row++;
            }
            else col++;
        }
        if (row >= 9) return true;
        int newRow = row+col/8;
        int newCol = (col+1)%9;
        for (int num = 1; num <= 9; num++) { // filled in with a number
            if (isValid(board, row, col, num)) {
                board[row][col] = (char)(num+'0');
                boolean result = solveSudokuHelper(board, newRow, newCol);
                if (result) return true;
                board[row][col] = '.'; // backtracking
            }
        }
        return false;
        
    }// end_solveSudokuHelper
    
    public boolean isValid(char[][] board, int row, int col, int num) {
        for (int i = 0; i < 9; i++) {  // check the row and col
            if (board[row][i] == num+'0' || board[i][col] == num+'0') return false;
        }
        // check square
        int rowoff = (row/3) * 3;
        int coloff = (col/3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[rowoff+i][coloff+j] == num+'0') return false;
            }
        } // end_for
        return true;
    }// end_isValid
}