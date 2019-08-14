class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        
        # dp[i][j]当前i  j区间里第一个玩家的得分，
        if n & 1:
            for i in range(n):
                f[i][i] = nums[i]  # n是奇数，那么最后一个数一定是第一个玩家来选
        
        for i in range(2, n+1):
            for j in range(n+1-i):
                # j, j+i-1
                l, r = j, j+i-1
                if (n-(r-l+1)) % 2 == 0:  # 代表玩家一先手
                    f[l][r] = max(f[l+1][r]+nums[l], f[l][r-1]+nums[r])
                else:   
                    # 否则就是对面先手，目的为了让玩家一的答案更小
                    f[l][r] = min(f[l+1][r], f[l][r-1])
                    
        sumn = 0
        for x in nums:
            sumn += x
        return f[0][n-1] >= sumn - f[0][n-1]