class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        Hash = collections.defaultdict(int)
        res = 0
        for blocks in wall:
            s = 0
            for i in range(len(blocks)-1):
                s += blocks[i]
                Hash[s] += 1
                res = max(res, Hash[s])
                
        return len(wall) - res