class Solution:
    def numTrees(self, n: int) -> int:
        # 卡特兰数
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        f = [0] * (n+1)
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] * (4*i-2) // (i+1)
        
        return f[n]