class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = collections.defaultdict(list)
        
        for p in prerequisites:
            self.graph[p[1]].append(p[0])
         # 状态， 0:未知， 1：正在访问， 2: 已经访问过
        self.v = [0] * numCourses
        
        ans = []
        
        for i in range(numCourses):
            if self.dfs(i, ans):
                return []
        ans.reverse()
        return ans
            
    def dfs(self, cur, ans):
        if self.v[cur] == 1:
            return True
        if self.v[cur] == 2:
            return False
        
        self.v[cur] = 1 # 正在访问
        for t in self.graph[cur]:
            if self.dfs(t, ans):
                return True
        self.v[cur] = 2
        ans.append(cur)
        
        return False