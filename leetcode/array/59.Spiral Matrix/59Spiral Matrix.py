'''
有规律的走四个方向，当在当前方向无法继续前进的时候
换一个新方向
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        
        visited = [[0] * n for _ in range(n)]
        #print(visited)
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        
        x, y, d = 0, 0, 1
        k = 1
        for _ in range(n*n):
            res[x][y] = k
            k += 1
            visited[x][y] = 1
            a, b = x+dx[d], y+dy[d]
            if not 0<=a<n or not 0<=b<n or visited[a][b]:
                d = (d+1) % 4
                a, b = x+dx[d], y+dy[d]
            
            x, y = a, b
            
        return res