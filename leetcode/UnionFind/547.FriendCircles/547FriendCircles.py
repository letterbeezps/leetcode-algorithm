class UniFind:
    def __init__(self, num):
        self.father = []
        for i in range(num):
            self.father.append(i)

    def getFather(self, n: int) -> int:
        if self.father[n] != n:
            self.father[n] = self.getFather(self.father[n])
        return self.father[n]
        
    def Union(self, a: int, b: int):
        fa = self.getFather(a)
        fb = self.getFather(b)
        self.father[fb] = fa

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        UF = UniFind(N)
        for i in range(N):
            for j in range(N):
                if M[i][j]:
                    UF.Union(i,j)
        #end_for
        res = 0
        for i in range(N):
            if UF.getFather(i) == i:
                res += 1
        return res
        