class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        return self.dfs(arr, start, len(arr), visited)
    
    def dfs(self, arr, i, n, visited):
        if i>=n or i<0 or visited[i]:
            return False
        if arr[i] == 0:
            return True
        visited[i] = True
        return self.dfs(arr, i-arr[i], n, visited) or self.dfs(arr, i+arr[i], n, visited)
        