class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rowIndex, colIndex = 0, len(matrix[0])-1
        while rowIndex < len(matrix) and colIndex >=0:
            if matrix[rowIndex][colIndex] == target:
                return True
            elif matrix[rowIndex][colIndex] > target:
                colIndex -= 1
            else:
                rowIndex += 1
                
        return False
        