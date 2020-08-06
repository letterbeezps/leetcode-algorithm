class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp[j] 加油j次后最远能到哪
        # dp[0] = startFuel
        # 01背包问题
        dp = [0] * (len(stations)+1)
        dp[0] = startFuel
        for i in range(0, len(stations)):
            for j in range(i+1, 0, -1):
                if dp[j-1] >= stations[i][0]:
                    dp[j] = max(dp[j], dp[j-1]+stations[i][1])
       
        for i, dpp in enumerate(dp):
            if dpp >= target:
                return i
        return -1