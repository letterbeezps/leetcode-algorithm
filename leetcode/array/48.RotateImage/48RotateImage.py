class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 一个8阶循环群
        n = len(matrix)
        # 先沿着主对角线翻转
        for i in range(n):
            j = i+1
            while j < n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j+=1
        # 再沿着垂直中线翻转
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]