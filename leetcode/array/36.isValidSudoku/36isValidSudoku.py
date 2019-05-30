class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    #check the board[i][j] is valid in i's row
                    for column in range(9):
                        if column != j and board[i][j] == board[i][column]:
                            return False
                    #check the board[i][j] is valid in j's column
                    for row in range(9):
                        if row != i and board[i][j] == board[row][j]:
                            return False
                    #check the board[i][j] is valid in the 3-by-3 box
                    for row in range((i // 3) * 3,(i // 3) * 3 + 3):
                        for col in range((j // 3) * 3,(j // 3) * 3 + 3):
                            if row != i and col != j and board[i][j] == board[row][col]:
                                return False
        return True