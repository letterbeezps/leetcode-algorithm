class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        for i in range(32):
            if x >> i or y >> i:
                if x >> i & 1 != y >> i & 1:
                    res += 1
        return res
        
#######################################################
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        t = x^y
        while t >0:
            res += t & 1
            t >>= 1
            
        return res
        