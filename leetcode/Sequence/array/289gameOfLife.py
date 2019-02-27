class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        """
        d --> d : 0
        l --> l : 1
        l --> d : 2
        d --> l : 3
        """
        row = len(board)
        col = len(board[0]) if row else 0  # 统计行数与列数
        dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]  # 用来寻找八个邻居
        for i in range(row):
            for j in range(col):
                cnt = 0
                for k in range(8):  # 遍历八个邻居
                    x, y = i + dir[k][0], j + dir[k][1]
                    if 0 <= x < row and 0 <= y < col:
                        if board[x][y] == 1 or board[x][y] == 2:
                            cnt += 1
                if board[i][j]: 
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 2  # 由生到死，当前为生
                elif not board[i][j] and cnt == 3:
                    board[i][j] = 3      # 由死到生，当前为死
                    
        for i in range(row):
            for j in range(col):
                board[i][j] %= 2  # 用取模运算计算下一个状态