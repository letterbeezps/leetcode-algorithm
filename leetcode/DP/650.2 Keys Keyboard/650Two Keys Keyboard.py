# 分析：copy paste copy 这样的操作是绝对不可取的，也就是说，最后一个操作一定是paste
#      copy paste copy paste = copy paste paste paste
# 任何一个状态都能从状态1 copy paste paste paste....得到
# 这其中有的状态：如状态9 可以从状态3 copy paste paste得到，降低了次数
class Solution: 
    def minSteps(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(2,n+1):
            for j in range(i-1,0,-1):
                if i%j==0:
                    dp[i]=dp[j]+i//j
                    break
        return dp[n]