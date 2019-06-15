class UniFind:
    def __init__(self, num):
        self.father = []
        for i in range(num):
            self.father.append(i)

    def getFather(self, n: int) -> int:
        if self.father[n] != n:
            self.father[n] = self.getFather(self.father[n])
        return self.father[n]
        
    def Union(self, a: int, b: int) -> bool:
        fa = self.getFather(a)
        fb = self.getFather(b)
        res = fa == fb
        if fa != fb:
            self.father[fb] = fa
        return res

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        UF = UniFind(N+1)  # 避免越界
        res = [0,0]
        for item in edges:
            u, v = item[0], item[1]
            if UF.Union(u, v):  # Redundant
                res = [u,v]
        #end_for
        return res
        