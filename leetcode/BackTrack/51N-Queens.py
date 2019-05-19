class Solution:
    def solveNQueens(self, _n: int) -> List[List[str]]:
        n = _n
        self.ans = []  # vector<vector<string>>
        paths = []     # vector<string>
        path = ['.'] * n  # record every path
        col = [False] * n
        diag = [False] * (2*n)
        anti_diag = diag + []
        
        def dfs(u: int):
            if u == n:
                paths1 = paths + []
                self.ans.append(paths1)
                return
            
            for i in range(n):
                #print(i)
                if not col[i] and not diag[u+n-i] and not anti_diag[u+i]:
                    col[i] = diag[u+n-i] = anti_diag[u+i] = True
                    path[i] = 'Q'
                    s = ''.join(path)
                    path[i] = '.'
                    paths.append(s)
                    dfs(u+1)
                    paths.pop()
                    col[i] = diag[u+n-i] = anti_diag[u+i] = False
        dfs(0)
        return self.ans