# 动态规划，状态表示
# f[i]  前i个字母能不能被字典表示
# f[i+j] =true 存在 f[i]==true and s[i:j+1] in dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        S = set(wordDict)
        
        n = len(s)
        f = [False] * (n+1)
        f[0] = True  # 没有字符，意味着可以被表示
        
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in S and f[j]:
                    f[i] = True
                    break
                    
        return f[n]