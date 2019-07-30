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



##############solution 2 heap###########
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret

################solution 3

from bisect import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if sum(bisect(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
                
        return lo