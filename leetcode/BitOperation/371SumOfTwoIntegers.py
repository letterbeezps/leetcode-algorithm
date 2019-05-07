'''
二进制表示
异或是一种不进位加法
而进位则要求两个两个数都是1
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        import ctypes  # python里int的范围很大，这里把它换成int32
        if not b:
            return a
        if not a:
            return b
        sum = a ^ b  # 先求不进位的结果
        carry = ctypes.c_int(a & b).value << 1  # 再求进位的结果
        return self.getSum(sum, carry)