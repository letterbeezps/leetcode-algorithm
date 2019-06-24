class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) != 9 or len(board[0]) != 9: return
        self.solveSudokuHelper(board, 0, 0)
    
    def isValid(self, board: List[List[str]], row: int, col: int, num: int) -> bool:
        for i in range(9):
            if board[row][i] == str(num) or board[i][col] == str(num):
                return False  # check the row and col
        row_index = (row // 3) * 3
        col_index = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[row_index+i][col_index+j] == str(num):
                    return False  # check the sub-boxes
        #end_for
        return True
    
    def solveSudokuHelper(self, board, row, col) -> bool:
        if not board or len(board) != 9 or len(board[0]) != 9: return False
        
        # find the first empty cell
        while row < 9 and col < 9:
            if board[row][col] == '.':
                break
            if col == 8:
                col = 0
                row += 1
            else: col += 1
        #end_while
        if row >= 9: return True
        newRow = row + col // 8
        newCol = (col + 1) % 9
        for num in range(1, 10):
            if self.isValid(board, row, col, num):
                board[row][col] = str(num)
                res = self.solveSudokuHelper(board, newRow, newCol)
                if res: return True
                board[row][col] = '.'
        #end_for
        return False
        