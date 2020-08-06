class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        for s in range(1-n, m):
            temp = []
            
            x = 0
            y = x-s
            while x < m and y < n:
                if y >= 0:
                    temp.append(mat[x][y])
                
                x += 1
                y += 1
            temp.sort()
            
            i = 0
            x = 0
            y = x-s
            while x < m and y < n:
                if y >= 0:
                    mat[x][y] = temp[i]
                    i += 1
                
                x += 1
                y += 1
        return mat