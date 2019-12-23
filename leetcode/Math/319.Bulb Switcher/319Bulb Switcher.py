# 先给每个灯泡编号 1---n
# 本质上是求每个编号的约数的个数，最后统计个数为奇数的结果。
# 约数个数为奇数等价于这个数是平方数
# 最后就是求1到n里面有多少个数是平方数
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)