class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        L_p, L_s = len(p), len(s)
        dp = [[0] * (L_p+1) for i in range(L_s+1)]  # 前i个s的字符串和p中j个字符串匹配与否
        dp[0][0] = 1
        for i in range(1, L_p+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
                
        for i in range(1, L_s+1):
            for j in range(1, L_p+1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] # 取j-1是把'*'当空字符i-1就是匹配任何字符串
        return bool(dp[L_s][L_p])
        