'''
x  = 1100101010
-x = 0011010110
&  = 0000000010

x & -x 等于x的二进制表示里的最右边的一个1
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & -n == n
        