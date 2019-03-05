class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        把矩阵分成两个部分，第一部分由第一行和第一列组成，剩下的次级矩阵为第二部分
        第一行和第一列的元素用来标记其所在的列或行是否置零
        在置零阶段从坐标（1，1）开始遍历
        第一行有col个元素，若该元素为0，则将其所在的列全部置零
        第一列同理
        最后处理第一行和第一列是否要置零
        """
        row = len(matrix)
        col = len(matrix[0])  # 现获取行数和列数
        rowIsZero = 0
        colIsZero = 0  # 先默认第一行和第一列无需置零
        
        for i in range(col):
            if matrix[0][i] == 0:
                rowIsZero = 1  # 第一行存在0，
                break
                
        for i in range(row):
            if matrix[i][0] == 0:
                colIsZero = 1  # 第一列存在0，
                break
                
        for i in range(1,row):
            for j in range(1,col):  # 从 1 1开始遍历次级矩阵
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0  # 如果matrix[i][j] == 0其所在的行列都为零
        
        # 置零阶段
        for i in range(1,row):
            for j in range(1,col):  # 从 1 1开始遍历
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0  # 置零
                    
        if rowIsZero:               # 最后处理第一行和第一列
             for i in range(col):
                matrix[0][i] = 0
                
        if colIsZero:
             for i in range(row):
                matrix[i][0] = 0