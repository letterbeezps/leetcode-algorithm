class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        size = 1 << n
        for i in range(size):
            res.append(self.binary_to_gray(i))
        return res
    
    def binary_to_gray(self, n):
        return n ^ (n >> 1)