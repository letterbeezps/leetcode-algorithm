class Node:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        
        # 定义状态，可以消除k个障碍到点x,y处，最少多少步
        dis = [[[m*n] * (k+1) for _ in range(n)] for _ in range(m)]  # 三维状态
        q = collections.deque()
        dis[0][0][0] = 0
        
        q.append(Node(0, 0, 0))
        
        while q:
            sta = q[0]
            if sta.x == m-1 and sta.y == n-1:
                return dis[sta.x][sta.y][sta.k]
            q.popleft()
            for i in range(4):
                tx, ty = sta.x+dx[i], sta.y+dy[i]
                if 0<=tx<m and 0<=ty<n:
                    if grid[tx][ty] == 1:
                        # 有障碍物
                        if sta.k < k and dis[tx][ty][sta.k+1] > dis[sta.x][sta.y][sta.k]+1:
                            # 转移条件：可以消除障碍物并且步数更优
                            dis[tx][ty][sta.k+1] = dis[sta.x][sta.y][sta.k]+1
                            q.append(Node(tx, ty, sta.k+1))
                    else:
                        # 没有障碍物：只要关心步数更优就行了
                        if dis[tx][ty][sta.k] > dis[sta.x][sta.y][sta.k]+1:
                            dis[tx][ty][sta.k] = dis[sta.x][sta.y][sta.k]+1
                            q.append(Node(tx, ty, sta.k))
        return -1