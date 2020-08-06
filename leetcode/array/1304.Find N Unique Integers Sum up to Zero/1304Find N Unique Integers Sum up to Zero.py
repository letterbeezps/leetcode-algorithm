class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        
        for i in range(n//2):
            res[i] = i+1
            res[i+n//2] = -i-1
        return res