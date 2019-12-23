class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = 0
        for i in grid:
            xy += len(i)
            
        xz = 0
        for lineX in grid:
            xz += max(lineX)
            
        yz = 0
        for j in range(len(grid)):
            tmp = 0
            for i in range(len(grid)):
                if grid[i][j] == 0:
                    xy -= 1
                tmp = max(tmp, grid[i][j])
            yz += tmp
        return xy+xz+yz