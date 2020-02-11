class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        # dijstra求最短路径
        pq = [(0, K)] # K到K 的距离为0，维护起始点到未访问节点的距离，距离无穷远的节点不加入
        dist = {}     # 结果，维护起始点到以确认顶点的距离
        while pq:
            d, node = heapq.heappop(pq)  # 小根堆
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:  # 跟新未访问节点，并且计算起始节点到它们的距离
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))
        return max(dist.values()) if len(dist)==N else -1


#########solution1#############
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((w, v))
            
        dist = {node: float('inf') for node in range(1, N+1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed+time)
        dfs(K, 0)
        ans = max(dist.values())
        
        return ans if ans < float('inf') else -1