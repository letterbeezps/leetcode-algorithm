class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 先找到最长公共子序列的dp矩阵
        l1, l2 = len(str1), len(str2)
        dp = [[0] * (l2+1) for i in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #end_for
        dd = collections.deque()
        while l1 or l2:
            c = ''
            if not l1:
                l2 -= 1
                c = str2[l2]
            elif not l2:
                l1 -= 1
                c = str1[l1]
            elif str1[l1-1] == str2[l2-1]:
                l1, l2 = l1-1, l2-1
                c = str1[l1]
            elif dp[l1-1][l2] == dp[l1][l2]:
                l1 -= 1
                c = str1[l1]
            elif dp[l1][l2-1] == dp[l1][l2]:
                l2 -= 1
                c = str2[l2]
            dd.appendleft(c)
        return ''.join(dd)