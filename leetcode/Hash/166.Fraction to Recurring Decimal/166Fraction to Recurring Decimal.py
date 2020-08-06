# get the fraction part
# (a%b)*10%b
# 每次将余数乘以10再除以除数，当同一个余数再次出现的时候，找到了循环结。
class Solution:
    def fractionToDecimal(self, _n: int, _d: int) -> str:
        # 先预处理负数
        n, d = abs(_n), abs(_d)
        minus = False
        if _n < 0: 
            minus = not minus
        if _d < 0:
            minus = not minus
        res = str(n//d)
        n %= d
        if not n:
            if minus and res != '0':
                return '-'+res
            return res
        res += '.'
        Hash = collections.defaultdict(int)
        
        while n:
            if Hash[n]:
                res = res[:Hash[n]] + '(' +res[Hash[n]:] + ')'
                break
            else:
                Hash[n] = len(res)
                n *= 10
                res += str(n//d)
                n %= d
        # end_while
        if minus:
            res = '-'+res
        return res
        
            