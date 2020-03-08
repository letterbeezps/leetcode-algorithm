class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        
        for p in prerequisites:
            self.graph[p[1]].append(p[0])
        
        # 状态， 0:未知， 1：正在访问， 2: 已经访问过
        self.v = [0] * numCourses
        
        for i in range(numCourses):
            if self.dfs(i):
                return False
        return True
    
    def dfs(self, cur):
        if self.v[cur] == 1:
            return True
        if self.v[cur] == 2:
            return False
        
        self.v[cur] = 1 # 正在访问
        for t in self.graph[cur]:
            if self.dfs(t):
                return True
        self.v[cur] = 2
        
        return False # 表示没有发现环