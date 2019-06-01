class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        L_g = len(g)
        L_s = len(s)
        i, j, res = 0, 0, 0
        for i in range(L_g):
            while j < L_s and s[j] < g[i]:
                j += 1
            if j < L_s:
                res += 1
                j += 1
        #end_for
        return res