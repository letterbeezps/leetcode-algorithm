class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        # 找连通分量
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [0] * n
        count = 0
        
        def dfs(cur: int):
            for u in graph[cur]:
                if not visited[u]:
                    visited[u] = 1
                    dfs(u)
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count-1