class Solution:
    def uniquePathsWithObstacles(self, nums: List[List[int]]) -> int:
        row = len(nums)
        col = len(nums[0])
        Dp = [[0] * col for i in range(row)]
        if not nums[0][0]:
            Dp[0][0] = 1
        
        for i in range(row):
            for j in range(col):
                if not nums[i][j]:
                    if i:
                        Dp[i][j] += Dp[i-1][j]
                    if j:
                        
                        Dp[i][j] += Dp[i][j-1]
            #end for
        #end for
        return Dp[row-1][col-1]
                
                    