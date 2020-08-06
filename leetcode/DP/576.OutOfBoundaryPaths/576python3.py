class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # f[i][j][k] means when the ball at i,j and we have k times, the number of paths
        f = [[[-1] * (N+1) for _ in range(n)] for _ in range(m)] # list(list(list(int)))
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        mod = 1000000007
        
        def dp(m: int, n: int, k: int, i: int, j: int) -> int:
            
            if f[i][j][k] != -1:
                return f[i][j][k]
            
            f[i][j][k] = 0
            if not k:
                return f[i][j][k]
            
            for q in range(4):
                a, b = i+dx[q], j+dy[q]
                if not 0<=a<m or not 0<=b<n:
                    f[i][j][k] += 1
                else:
                    f[i][j][k] += dp(m, n, k-1, a, b)
                f[i][j][k] %= mod
            return f[i][j][k]
            
        return dp(m, n, N, i, j)