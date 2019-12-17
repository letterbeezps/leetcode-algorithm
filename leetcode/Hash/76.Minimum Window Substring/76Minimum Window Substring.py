# 双指针搜索

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # from collections import Counter, defaultdict
        T = collections.Counter(t)
        S = collections.defaultdict(int)
        
        res = ''
        total = len(T)
        satisfy = 0
        j = 0
        for i in range(len(s)):
            S[s[i]] += 1
            if S[s[i]] == T[s[i]]:  # 当前这个 i是有用的
                satisfy += 1
            while j < len(s) and S[s[j]] > T[s[j]]:
                S[s[j]] -= 1
                j += 1
            if satisfy == total and (not res or i-j+1 < len(res)):
                res = s[j:i+1] 
        return res