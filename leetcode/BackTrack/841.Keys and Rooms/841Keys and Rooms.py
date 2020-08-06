class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = collections.defaultdict(int)
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
        
    def dfs(self, rooms, cur, visited):
        if visited[cur]:
            return
        visited[cur] += 1
        for i in rooms[cur]:
            self.dfs(rooms, i, visited)