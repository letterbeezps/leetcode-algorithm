'''
有规律的走四个方向，当在当前方向无法继续前进的时候
换一个新方向
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        n, m = len(matrix), len(matrix[0])
        visited = [[0] * m for i in range(n)]
        #print(visited)
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        x, y, d = 0, 0, 1
        for k in range(n*m):
            res.append(matrix[x][y])
            visited[x][y] = 1
            a, b = x+dx[d], y+dy[d]
            if not 0<=a<n or not 0<=b<m or visited[a][b]:
                d = (d+1) % 4
                a, b = x+dx[d], y+dy[d]
            
            x, y = a, b
            
        return res