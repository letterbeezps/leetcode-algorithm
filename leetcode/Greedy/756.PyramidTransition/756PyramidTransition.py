class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.allows = collections.defaultdict(str)
        for x in allowed:
            a,c = x[0] + x[1],x[2]
            self.allows[a] += c
            
        return self.dfs(bottom, '')
    
    def dfs(self, last: str, now: str):
        if len(last) == 1:
            return True
        if len(now) + 1 == len(last):  # 当前这一层枚举结束
            return self.dfs(now, '')
        
        a, b = last[len(now)], last[len(now) + 1]
        
        for c in self.allows[a+b]:
            if self.dfs(last, now+c):
                return True
        #end_for
        return False
                        
            