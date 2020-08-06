'''
把a的最后一个字符变成b的最后一个字符
case1:  a1 a2 a3 ... am bn
        b1 b2 b3 ... bn       f[m][n] = f[m][n-1]+1
case2:  a1 a2 a3 ... am-1 am
        b1 b2 b3 ... bn-1 bn  f[m][n] = f[m-1][n]+1
case3:  a1 a2 a3 ... am-1 am
        b1 b2 b3 ... bn-1 bn  f[m][n] = f[m-1][n-1]+1  am replace bn
case4:  a1 a2 a3 ... am-1 am
        b1 b2 b3 ... bn-1 bn  f[m][n] = f[m-1][n-1]    am = bn
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = [[None] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        return f[m][n]