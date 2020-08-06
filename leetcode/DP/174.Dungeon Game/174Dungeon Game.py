class Solution:
    def calculateMinimumHP(self, dg: List[List[int]]) -> int:
        m, n = len(dg), len(dg[0])
        # print(m, n)
        # 从右下角到x,y所需的最小hp
        dp = [[2**31] * (n+1) for _ in range(m+1)]
        
        dp[m][n-1] = dp[m-1][n] = 1 # 小于等于0都是失败，所以最小是1
        
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                dp[x][y] = max(1, min(dp[x][y+1], dp[x+1][y])-dg[x][y])
                
        return dp[0][0]