class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
       # dp定义成有多少酒流过这个杯子
        kRows = 100
        dp = [[0] * kRows for _ in range(kRows)]
        dp[0][0] = poured
        for i in range(kRows-1):
            for j in range(i+1):
                if dp[i][j] > 1:
                    dp[i+1][j] += (dp[i][j]-1) / 2.0
                    dp[i+1][j+1] += (dp[i][j]-1) / 2.0
        return min(1.0, dp[query_row][query_glass])
        