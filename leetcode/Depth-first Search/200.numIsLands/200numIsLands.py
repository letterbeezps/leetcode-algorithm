'''
look back on 733th
The question is essentially looking for 
the number of connected graphs in a graph
If we find a '1', we replace all elements in the connected graph of this '1' with '0' and res++
Then continue to traverse this arraya
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return 0
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(self.row):
            for j in range(self.col):  # 遍历整个矩阵
                if grid[i][j] == '1':    
                    res += 1
                    self.dfs(grid, i, j)
        #end for
        return res
        
    # 把被访问过的小岛全部变成水
    def dfs(self, grid: List[List[str]], x: int, y: int):
        d = [[0,-1],[-1,0],[0,1],[1,0]]  # 周围的四个邻居
        grid[x][y] = '0'
        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if 0<=nx<self.row and 0<=ny<self.col:
                if grid[nx][ny] == '1':
                    self.dfs(grid, nx, ny)