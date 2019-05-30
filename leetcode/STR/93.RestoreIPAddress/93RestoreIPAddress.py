class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []  # 记录结果
        path = ''  # 合法的IP地址
        self.dfs(s, 0, 0, path)
        return self.res
    
    def dfs(self, s: str, u, k, path: str):  # u当前遍历到哪一位，k：path里网段的个数，合法的k为4
        # 判断合法
        if u == len(s):
            if k == 4:
                self.res.append(path[1:])
            return
        
        if k > 4:
            return
        
        if s[u] == '0':
            self.dfs(s, u+1, k+1, path+'.0')
        else:
            t = 0
            for i in range(u, len(s)):
                t = t * 10 + int(s[i])
                if t < 256:
                    self.dfs(s, i+1, k+1, path+'.'+str(t))
                else:
                    break