'''
path, path's number is k
1 2 3 .... n
start with 1
dfs(path, 1, n, k)
'''
class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = list()
        path = list()
        self.dfs(path, 1, n, k)
        return self.res
        
    def dfs(self, path: list, start: int, n: int, k: int):
        if not k:
            t = []
            for x in path:
                t.append(x)
            self.res.append(t)
            return
        for i in range(start, n+1):
            path.append(i)
            self.dfs(path, i+1, n, k-1)
            path.pop()
################################################################
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        nums = [i+1 for i in range(n)]
        self.helper(nums, k, [])
        return self.res
        
    def helper(self, nums, k, cur):
        if k == 0:
            self.res.append(cur)
            return
        for i in range(len(nums)-k+1):
            self.helper(nums[i+1:], k-1, cur + [nums[i]])