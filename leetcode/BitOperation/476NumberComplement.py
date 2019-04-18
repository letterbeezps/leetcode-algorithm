'''
当作二进制来考虑
问题的关键在 no leading zero bit in integer's binary representation
这个可以用和1做取与运算来解决

'''
class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        t = 0  # t代表进制,
        while num:
            bit = 0 if (num & 1) else 1  # 取二进制的个位，并且取反，不能用“～”来取反
            res += bit << t  # 把bit放到对应的位置
            num >>= 1  # num再右移一位
            t += 1 
        #end_while
        return res