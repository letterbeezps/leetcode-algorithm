# 记忆化递归
class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        self.mem_ = {}
        return self.ways(s)
        
    def ways(self, s: str):
        if s in self.mem_:
            return self.mem_[s]
        
        ans = []
        for i in range(len(s)):
            op = s[i]
            if op=='+' or op=='-' or op=='*':
                left = s[:i]
                right = s[i+1:]
                
                l = self.ways(left)
                r = self.ways(right)
                
                # 笛卡尔积
                for a in l:
                    for b in r:
                        ans.append(self.zp_use(op, a, b))
        if not ans:
            ans.append(int(s))
        self.mem_[s] = ans
        return self.mem_[s]
                
    def zp_use(self, op: str, a, b):
        if op == '*':
            return a*b
        if op == '+':
            return a+b
        if op == '-':
            return a-b
        