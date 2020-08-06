'''
记忆化搜索
动态规划
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        row, col = len(matrix), len(matrix[0])
        f = [[-1] * col for i in range(row)]
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        
        def dp(x, y, matrix) -> int:
            if f[x][y] != -1:
                return f[x][y]
            f[x][y] = 1
            for i in range(4):
                a, b = x+dx[i], y+dy[i]
                if 0<=a<row and 0<=b<col and matrix[a][b] > matrix[x][y]:
                    f[x][y] = max(f[x][y], dp(a, b, matrix) + 1)
            return f[x][y]
        
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, dp(i, j, matrix))
        return res