class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        
        area = 0
        conn = 0
        
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    area += 1
                    if y > 0 and grid[y-1][x] == 1:
                        conn += 1
                    # if y < m-1 and grid[y+1][x] == 1:
                    #     conn += 1
                    if x > 0 and grid[y][x-1] == 1:
                        conn += 1
                    # if x < n-1 and grid[y][x+1] == 1:
                    #     conn += 1
        return area*4 - conn*2