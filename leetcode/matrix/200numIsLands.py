'''
look back on 733th
The question is essentially looking for 
the number of connected graphs in a graph
If we find a '1', we replace all elements in the connected graph of this '1' with '0' and res++
Then continue to traverse this arraya
'''
class Solution:
    row = 0
    col = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return 0
        Solution.row = len(grid)
        Solution.col = len(grid[0])
        for i in range(Solution.row):
            for j in range(Solution.col):  # 遍历整个矩阵
                if grid[i][j] == '1':    
                    res += 1
                    self.dfs(grid, i, j)
        #end for
        return res
        
    def dfs(self, grid: List[List[str]], x: int, y: int):
        dir = [[0,-1],[-1,0],[0,1],[1,0]]  # 周围的四个邻居
        grid[x][y] = '0'
        for i in range(4):
            nx = x+dir[i][0]
            ny = y+dir[i][1]
            if 0<=nx<Solution.row and 0<=ny<Solution.col:
                if grid[nx][ny] == '1':
                    self.dfs(grid, nx, ny)