class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.no_ans = 1
        if not matrix or not matrix[0]:
            self.no_ans = 0
        else:
            M, N = len(matrix), len(matrix[0])
            A = [[0] * (N+1) for _ in range(M+1)]
            for x in range(M):
                for y in range(N):
                    A[x+1][y+1] = A[x][y+1] + A[x+1][y] + matrix[x][y] - A[x][y]
            self.A = A
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.no_ans:
            return self.A[row2+1][col2+1] - self.A[row2+1][col1] - self.A[row1][col2+1] + self.A[row1][col1]
        else:
            return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)