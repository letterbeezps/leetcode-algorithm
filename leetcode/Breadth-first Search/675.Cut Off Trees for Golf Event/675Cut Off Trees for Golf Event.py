class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # 最短路径问题，每次找两棵树之间的最短路径floyd？？？？
        m, n = len(forest), len(forest[0])
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]
        self.m, self.n = m, n
        
        trees = []
        for y in range(m):
            for x in range(n):
                if forest[y][x] > 1:
                    trees.append((forest[y][x], x, y))
        trees.sort()  # 根据高度排序，树的高度都不相同
        
        sx, sy = 0, 0
        total_steps = 0
        
        for i in range(len(trees)):
            tx, ty = trees[i][1], trees[i][2]  # 每次只能砍当前最矮的树
            
            steps = self.BFS(forest, sx, sy, tx, ty)
            if steps == 2**31-1: return -1
            
            forest[ty][tx] = 1
            
            total_steps += steps
            sx, sy = tx, ty
        return total_steps
    
    def BFS(self, forest, sx, sy, tx, ty):
        visited = [[0] * self.n for _ in range(self.m)] # 
        q = collections.deque()  # queue((x, y))
        q.append((sx, sy))  # 当前起点
        steps = 0
        while q:
            new_nodes = len(q)
            while new_nodes:   # bfs当前节点能够访问的全部下一个节点
                node = q.popleft()
                cx, cy = node
                if cx==tx and cy==ty:
                    return steps
                for i in range(4):
                    x, y = cx+self.dx[i], cy+self.dy[i]
                    if not 0<=x<self.n or not 0<=y<self.m or not forest[y][x] or visited[y][x]:
                        continue
                    visited[y][x] = 1
                    q.append((x,y))
                
                new_nodes -= 1
            steps += 1
        return 2**31-1
        
        
        
        
        
        