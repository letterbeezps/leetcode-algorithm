'''
直观思路：把二维矩阵展开为一行，再处理
hint这个矩阵的左上角的树最小，右下角的数最大，可以用这个特点来二分
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def count(matrix: List[List[int]], target) -> int:
            # 统计矩阵中小于target的数的个数
            n = len(matrix)
            i, j = n-1, 0
            res = 0
            # 从第0列，最底层开始计数
            while i >= 0 and j < n:
                if matrix[i][j] < target:
                    res += i+1
                    j += 1
                else:
                    i -= 1
            return res
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left+1 < right:
            mid = left + (right - left) // 2
            print(mid)
            num = count(matrix, mid)
            if num >= k:
                right = mid
            else:
                left = mid
        #end_while
        
        if count(matrix, right) <= k-1:
            return right
        else:
            return left