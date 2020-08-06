class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        c = [[False] * n for _ in range(n)]
        
        # 为了判断回文子串
        for i in range(1, n+1):
            for j in range(n+1-i):
                l, r = j, j+i-1
                tag = l+1 > r-1 or c[l+1][r-1]
                c[l][r] = s[l] == s[r] and tag
                
        f = [2**31] * (n+1)
        f[0] = 0  # 保证从f[0]转移
        for i in range(1, n+1):
            for j in range(1, i+1):
                if c[j-1][i-1]:
                    f[i] = min(f[i], f[j-1]+1)
                    
        # print(c)
                    
        return f[n]-1
        
        
    