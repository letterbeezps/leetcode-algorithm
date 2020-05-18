class Solution:
    def numOfWays(self, n: int) -> int:
        kMod = 1e9 + 7

        dp = [[6] * 2 for _ in range(n+1)]
        # 上色的方法有使用三种颜色或使用两种颜色，两种上色思路
        # dp[i][0] 第i行用两种颜色上色的方法
        # dp[i][1] 第i行用三种颜色上色的方法
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] * 3 + dp[i-1][1] * 2) % kMod
            dp[i][1] = (dp[i-1][0] * 2 + dp[i-1][1] * 2) % kMod

        return int((dp[n][0] + dp[n][1]) % kMod)