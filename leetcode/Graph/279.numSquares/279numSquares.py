'''
图论问题
BFS
0到n看作N+1个点，
若一个点的值加上一个平方数能到另外一个一点
那么在两个点之间连一条边，且权值为1
问题就变成了从0点到n点的最短距离
'''
import sys, collections
class Solution:
    def numSquares(self, n: int) -> int:
        INT_MAX = sys.maxsize
        q = collections.deque()
        dist = [INT_MAX] * (n+1)  # 用来记录距离
        dist[0] = 0  # 0节点到0 的距离就是0
        q.append(0)  # 起始节点是0节点
        while q:
            t = q[0]
            q.popleft()
            if t == n:
                return dist[t]
            i = 1
            while t+i*i <= n:  # 找到当前节点所有的子节点
                j = t+i*i
                if dist[j] > dist[t]+1:  # 现在已经确定节点j到节点t的距离为1
                    dist[j] = dist[t] + 1
                    q.append(j)
                i += 1
            #end while_1
        #end while_2
        return 0