class Solution:
    def toHex(self, num: int) -> str:
        div = 0
        mod = 0
        res = ''
        trans = ['a','b','c','d','e','f']
        if not num:
            return '0'
        if num < 0:
            num += 2**32  # 负数对应的正数
        while num > 0:
            if num % 16 >= 10:
                res += trans[num%16-10]
            else:
                res += str(num%16)
            num //= 16
        return res[::-1]