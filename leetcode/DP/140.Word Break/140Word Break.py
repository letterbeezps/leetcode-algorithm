class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # self.ans = []
        self.mem_ = {} # 记忆答案
        S = set(wordDict)
        return self.dfs(s, S)
        
    def append(self, prefixes, word):
        res = [] # [str]
        for pre in prefixes:
            res.append(pre + ' ' + word)
        return res
        
    def dfs(self, s, S):
        if s in self.mem_:
            return self.mem_[s]
        ans = []
        if s in S:
            ans.append(s)
        for i in range(1, len(s)):
            right = s[i:]
            if right not in S:
                continue
            left = s[:i]
            left_ans = self.append(self.dfs(left, S), right)
            
            for item in left_ans:
                ans.append(item)
        self.mem_[s] = ans
        ans = []
        return self.mem_[s]
        
        