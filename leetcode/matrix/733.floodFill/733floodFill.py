'''
在网格中找到连通块
适合DFS
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image  # 如果数组为空，
        dir = [[0,-1],[-1,0],[0,1],[1,0]]  # 周围的四个邻居
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image  # 格子的颜色和新颜色一样就直接返回不需要处理，否则后面会爆栈
        
        image[sr][sc] = newColor
        
        for i in range(4):
            x = sr+dir[i][0]
            y = sc+dir[i][1]
            if 0<=x<len(image) and 0<=y<len(image[0]):
                if image[x][y] == oldColor:
                    self.floodFill(image,x,y,newColor)
        #end for
        return image
        