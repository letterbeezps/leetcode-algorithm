class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost.copy()
        dp.append(0)
        n = len(cost)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + dp[i]
        return dp[-1]