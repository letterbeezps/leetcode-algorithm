class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m = int(c ** 0.5)
        for a in range(m+1):
            b = round((c-a**2) ** 0.5)
            
            if a**2 + b**2 == c:
                return True
        return False