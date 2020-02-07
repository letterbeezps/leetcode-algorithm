class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        f = [[0] * m for _ in range(n)]
        
        f[0] = A[0]
        
        for i in range(1, n):
            for j in range(m):
                f[i][j] = f[i-1][j] + A[i][j]
                if j>0:
                    f[i][j] = min(f[i][j], f[i-1][j-1]+A[i][j])
                if j<m-1:
                    f[i][j] = min(f[i][j], f[i-1][j+1]+A[i][j])
        return min(f[n-1])
        