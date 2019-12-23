'''
Python 关于整除以及负数取余遇到的问题
'''
class Solution:
    def reverse(self, x: int) -> int:
        t = 1
        if x < 0:
            t = -1
        res = 0
        x = abs(x)
        while x != 0:
            newres = res * 10 + x % 10
            res = newres
            if not (-2147483648< res*t < 2147483647):
                return 0
            x //= 10
        return res*t