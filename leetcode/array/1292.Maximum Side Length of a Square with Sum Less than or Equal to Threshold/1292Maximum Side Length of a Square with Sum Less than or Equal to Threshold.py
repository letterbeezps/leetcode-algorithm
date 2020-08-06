class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # 二维的前缀和
        m, n = len(mat), len(mat[0])
        
        sumn = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                sumn[i][j] = sumn[i-1][j] + sumn[i][j-1] - sumn[i-1][j-1] + mat[i-1][j-1]
                
        def check(s):
            for i in range(1, m-s+2):
                for j in range(1, n-s+2):
                    x, y = i+s-1, j+s-1
                    if sumn[x][y] - sumn[i-1][y] - sumn[x][j-1] + sumn[i-1][j-1] <= threshold:
                        # 画图，一目了然
                        return True
            return False
                
        l, r = 1, min(m, n)
        while l < r:
            mid = l+r >> 1
            if check(mid+1):
                l = mid+1
            else:
                r = mid
        if check(l):
            return l
        
        return 0