# 维护已经划分好的区间列表，正在枚举的区间，枚举的下标，s
# 如果已经遍历结束，判断当前区间是否回文
# 若没有结束，1、now不是回文，在now上加字符。2、now是回文，开辟新区间和加字符都要执行（不同状态）。
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = [] # list(list(str))
        self.path = [] # list(str)
        
        self.dfs(s, 0, '')
        return self.ans
    
    def check(self, now: str):
        if not now:
            return False
        return now == now[::-1]
        
    
    
    def dfs(self, s: str, index, now: str):  # now表示已经枚举完的区间
        if index == len(s):
            if self.check(now):
                self.path.append(now)
                self.ans.append(self.path[:])
                self.path.pop()
            return
        if self.check(now):
            self.path.append(now)
            self.dfs(s, index, '')
            self.path.pop()
        self.dfs(s, index+1, now+s[index])
        