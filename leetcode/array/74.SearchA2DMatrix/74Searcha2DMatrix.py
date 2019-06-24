'''遍历所有数据'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix):
            return False
        n = len(matrix[0])
        left = 0
        right = len(matrix) * n -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[mid//n][mid%n]:
                return True
            elif target < matrix[mid//n][mid%n]:
                right = mid-1
            else:
                left = mid+1
        return False


######################################
#######222222222222###################
'''遍历一行一列'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m-1
        target_row = None
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][n-1] == target:
                target_row = mid
                break
            elif matrix[mid][n-1] < target:
                left = mid + 1
            else:
                right = mid-1
                
        if target_row == None: 
            target_row = left
        if target_row == m:
            return False
        
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False