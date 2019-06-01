class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res, tag = '', ''
        if num<0:
            tag = '-'
            num = abs(num)
        while num:
            res = str(num%7) + res
            num //= 7
        return tag+res