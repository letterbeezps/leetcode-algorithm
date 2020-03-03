class Solution:
    def printVertically(self, s: str) -> List[str]:
        v = s.split()
        m = 0
        for item in v:
            m = max(m, len(item))
            
        ans = []
        t = ''
        for j in range(m):
            for i, item in enumerate(v):
                if j < len(item):
                    t += item[j]
                else:
                    t += ' '
            ans.append(t.rstrip())
            t = ''
        return ans 
        