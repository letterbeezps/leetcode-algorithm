## 等差数列求和

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        k = 1
        while k*(k-1) < 2*N:
            if 2*N % k == 0 and (2*N//k-k+1) % 2 == 0:
                res += 1
            
            k += 1
        return res