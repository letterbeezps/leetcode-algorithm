class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        
        a = [[0] * m for _ in range(n)]
        p = [[0] * m for _ in range(n)]
        
        def dfs(x, y, h, v):
            if x<0 or y<0 or x==m or y==n:
                return
            if v[y][x] or matrix[y][x] < h:
                return
            v[y][x] = 1
            dfs(x+1, y, matrix[y][x], v)
            dfs(x-1, y, matrix[y][x], v)
            dfs(x, y-1, matrix[y][x], v)
            dfs(x, y+1, matrix[y][x], v)
            
        for x in range(m):
            dfs(x, 0, 0, p)
            dfs(x, n-1, 0, a)
        for y in range(n):
            dfs(0, y, 0, p)
            dfs(m-1, y, 0, a)
         
        ans = []
        for i in range(n):
            for j in range(m):
                if p[i][j] and a[i][j]:
                    ans.append([i, j])
        return ans