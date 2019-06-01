class Solution:
    def totalNQueens(self, _n: int) -> int:
        self.ans = 0
        n = _n
        col = [False] * n
        diag = [False] * (2*n)
        anti_diag = diag + []
        
        def dfs(u: int):
            if u == n:
                self.ans += 1
                return
            for i in range(n):
                #print(i)
                if not col[i] and not diag[u+n-i] and not anti_diag[u+i]:
                    col[i] = diag[u+n-i] = anti_diag[u+i] = True
                    dfs(u+1)
                    col[i] = diag[u+n-i] = anti_diag[u+i] = False
        dfs(0)
        return self.ans
                    