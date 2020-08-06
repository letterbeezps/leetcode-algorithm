class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # f[i][j] 表示以ij为右下角的正方形d的边最大是多少
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
                    if i and j:
                        dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    res = max(res, dp[i][j])
        # 
                    
        return res*res