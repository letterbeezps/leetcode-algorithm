'''
0  01  10  11  100  101
0  1   2   3   4    5
0  1   1   2   1    2
如果元素是2的次幂，那它的二进制表示就是1000.。。。。的形式
再给一个例子： A：1001001001001
             B：100100100100
             A和B的二进制表示里1的个数之差一个，只要把B向左移一位再末位加一就是A，左移等于翻倍
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        f = [0] * (num+1)
        f[0] = 0
        for i in range(num+1):
            f[i] = f[i // 2] + (i & 1)
        return f