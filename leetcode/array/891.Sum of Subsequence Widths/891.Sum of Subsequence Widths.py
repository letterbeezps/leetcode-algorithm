# math question
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 1000000007
        A.sort()
        res = 0
        p = 1
        sumn = 0
        for x in A:
            res = (res + x * (p-1) - sumn)%mod
            sumn = (sumn*2 + x) % mod
            p = p*2 % mod
            
        return (res+mod)%mod