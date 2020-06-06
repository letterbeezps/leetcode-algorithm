class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # 动态规划
        # dp(m,n,k)k步之内划分矩阵pizza[m:M][n:N]的方法
        # 将大矩阵的解化为小矩阵的解
        kMod = 1e9+7
        M, N = len(pizza), len(pizza[0]) # M行，N列
        A = [[0] * (N+1) for _ in range(M+1)]
        for x in range(M):
            for y in range(N):
                A[x+1][y+1] = A[x+1][y] + A[x][y+1] + (pizza[x][y] == 'A') - A[x][y]
        def hasApple(x1, y1, x2, y2):
            return (A[x2+1][y2+1] - A[x2+1][y1] - A[x1][y2+1] + A[x1][y1]) > 0
        # print(A)

        cache = [[[-1] * k for j in range(N)] for i in range(M)]
        def dp(m, n, k):
            if not k:
                return 1 if hasApple(m, n, M-1, N-1) else 0
            if cache[m][n][k] != -1:
                return cache[m][n][k]
            cache[m][n][k] = 0
            for x in range(m, M-1):
                cache[m][n][k] = (cache[m][n][k] + hasApple(m, n, x, N-1) * dp(x+1, n, k-1)) % kMod
            for y in range(n, N-1):
                cache[m][n][k] = (cache[m][n][k] + hasApple(m, n, M-1, y) * dp(m, y+1, k-1)) % kMod
            return int(cache[m][n][k])
        return dp(0,0,k-1)