import functools
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # 两个问题
        # 把一个字符串变成回文，最少要几步
        # 分成k组最优解是多少
        # 动态规划 加 记忆化搜索, dp(i, k)把长度为i的字符串分成k组回文串的最小代价
        @functools.lru_cache(None)
        def cost(i, j):
            if i >= j:
                return 0
            return cost(i+1, j-1) + (1 if s[i]!=s[j] else 0)
        
        @functools.lru_cache(None)
        def dp(i, k):  # 0--i 分成k份
            if k==1:   # 1份只要原串回文就行了
                return cost(0, i)
            if k == i+1:  # 分成k+1份，即分成每个字符就行了
                return 0
            if k > i+1:   # 不合法
                return 2**31-1
            return min([dp(j, k-1) + cost(j+1, i) for j in range(i)])
        
        return dp(len(s)-1, k)
        