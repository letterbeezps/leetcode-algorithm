# 总面积减去交集的面积
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        X = min(C, G) - max(A, E)
        Y = min(D, H) - max(B, F)
        return (C-A)*(D-B)+(G-E)*(H-F) - max(0, X)*max(0,Y)