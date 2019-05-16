'''
动态规划的分析
s = abcdedfg  p = abcde.*
构建一个状态矩阵dp[][]记录匹配是否成功。
dp[i][j]s中取第1-i个字符是否匹配p中第1-j个字符，从起点0开始

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        L_s, L_p = len(s), len(p)
        if s is None or p is None:
            return False
        dp = [[0] * (L_p+1) for i in range(L_s+1)]  # s中取第1-i个字符是否匹配p中第1-j个字符
        dp[0][0] = 1  # s的前0位和p的前0位肯定匹配，同理s的前ℹ位和p的前0位肯定不匹配
        for i in range(1,L_p+1):  # 这是关键的一步初始化
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        
        
        for i in range(1,L_s+1):   # 再分三种状态更新状态矩阵
            for j in range(1,L_p+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        
        return True if dp[L_s][L_p] else False