'''
依然是寻找连通图的问题
先遍历数组四周，对边缘上为'o'的元素做DFS连通遍历，再把找到的连通图里的元素全部换成'Y'
接着再遍历整个数组，把数组里'O'元素换成'X'，'Y'元素换成'O'
结束
'''
class Solution:
    row = 0
    col = 0
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        Solution.row = len(board)
        Solution.col = len(board[0])
        
        for i in range(Solution.row):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][Solution.col-1] == 'O':
                self.dfs(board, i, Solution.col-1)
                
        for i in range(Solution.col):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
            if board[Solution.row-1][i] == 'O':
                self.dfs(board, Solution.row-1, i)
                
        for i in range(Solution.row):
            for j in range(Solution.col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
        
    def dfs(self, board: List[List[str]], x: int, y: int):
        dir = [[0,-1],[-1,0],[0,1],[1,0]]  # 周围的四个邻居
        board[x][y] = 'Y'
        for i in range(4):
            nx = x+dir[i][0]
            ny = y+dir[i][1]
            if 0<=nx<Solution.row and 0<=ny<Solution.col:
                if board[nx][ny] == 'O':
                    self.dfs(board, nx, ny)