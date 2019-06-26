'''
二分法：x^n = (x^2)^(n//2)  if n % 2 == 0
奇偶2^9，  res:      num     pow
          1         2       9
          2         2       8   :偶数了
          2         4       4
          2         16      2
          2         256     1   : 2 * 256
负数2^-2 = 1 / 2^2
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        import ctypes
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / (x*self.myPow(x, -(n+1)))
        res = 1.0
        while n > 1:
            if n%2 == 1:
                res *= x
            x = x * x
            n //= 2
        res *= x
        return res