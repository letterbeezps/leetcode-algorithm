import collections
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        如果本身是“0”，它到“0”节点的距离就是0
        邻居节点到最近0的距离不会超过自己到最近0距离值加一
        '''
        INT_MAX = 10001
        row = len(matrix)
        col = len(matrix[0])
        dir = [[0,-1],[-1,0],[0,1],[1,0]]  # 周围的四个邻居
        
        q = collections.deque()  # 用来存储节点的坐标
        temp = []  # 接收队列的头节点
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0: #初始化，将坐标存储在队列中
                    q.append([i,j])
                else:
                    matrix[i][j] = INT_MAX         
        while q:
            temp = q[0]
            q.popleft()  # 取头节点后再弹出节点
            for i in range(4):
                x = temp[0]+dir[i][0]
                y = temp[1]+dir[i][1]
                if 0<=x<row and 0<=y<col:  # 处理边界节点
                    if matrix[x][y] <= matrix[temp[0]][temp[1]] + 1:
                        continue
                    # 邻居节点到最近0距离过长
                    else:
                        matrix[x][y] = matrix[temp[0]][temp[1]] + 1
                        q.append([x,y])        
        return matrix