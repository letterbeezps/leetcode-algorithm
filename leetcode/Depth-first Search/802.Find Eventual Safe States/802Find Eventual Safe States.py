class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0：未知， 1:正在访问 2:安全 3:不安全
        self.v = [0] * n
        ans = []
        for i in range(n):
            if self.dfs(graph, i) == 2:
                ans.append(i)
        ans.sort()
        
        return ans
    
    def dfs(self, graph, cur):
        if self.v[cur] == 1:
            return 3  # 碰到环了
        if self.v[cur] != 0:
            return self.v[cur]
        
        self.v[cur] = 1  # 标为正在访问
        for nxt in graph[cur]:
            if self.dfs(graph, nxt) == 3:
                self.v[cur] = 3
                return 3
        self.v[cur] = 2
        return 2
                