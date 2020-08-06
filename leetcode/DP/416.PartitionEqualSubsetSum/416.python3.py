'''
这是一个01背包问题，在分析完数据后，就是在列表里寻找一组子集
使得它们的和是总和的一半，01背包，只分取或不取两种情况。
解法1，先给出通用01背包模版解法，效率和空间都不是很好，解法二会给出优化方案
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        sumn = sum(nums)
        
        if sumn % 2 == 1:
            return False
        
        sumn //= 2
        n = len(nums)
        
        dp = [[0] * (sumn+1) for i in range(n+1)]
        # dp[i][j]  表示前i个数中能否找到子集的和为j
        dp[0][0] = 1
        for i in range(n+1):
            dp[i][0] = 1
            
        for j in range(1, sumn+1):
            dp[0][j] = 0
            
        for i in range(1, n+1):
            for j in range(1, sumn+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return True if dp[n][sumn] else False

###########solution 2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        sumn = sum(nums)
        
        if sumn % 2 == 1:
            return False
        
        sumn //= 2
        n = len(nums)
        
        dp = [0] * (sumn+1)
        dp[0] = 1
            
        for i in range(1, n+1):
            for j in range(sumn, nums[i-1]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i-1]]
                    
        return True if dp[sumn] else False