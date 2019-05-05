'''
m     = 10101010011
n_max = 10101100000

如果n大于等于n_max,那么在第五位上的全部  与  运算的值都是0，反之为1
问题就变成如何求指定未上的n_max
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        i = 0
        while (1 << i) <= m:
            if m >> i & 1:
                if (m & ~((1 << i) - 1)) + (1 << i) > n:
                    res += 1 << i
            #end_if
            i += 1
        #end_while
        return res