class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n, m = len(arr), len(arr[0])
        INF = 2**31-1
        f = [[INF] * m for _ in range(n)]
        
        f[0] = arr[0]
        # 暴力
        
        for i in range(1, n):
            for j in range(m):
                for k in range(m):
                    if j != k:
                        f[i][j] = min(f[i][j], f[i-1][k]+arr[i][j])
                        
        return min(f[n-1])
    # 还可以预处理数据，减少时间，以第i+1行为例子
    # 如果想要得到到arrp[i+1][j]的最短距离
    # 那么这个结果就是f[i+1][j] = min( min(f[i][0...j-1]), min(j+1...m-1) ) + arr[i+1][j]
    # 没意义o.o
        
        