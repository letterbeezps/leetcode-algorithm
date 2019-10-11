class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1  # 这是必然，没有其他分法了
        # N = n1 + n2 + n3 + ... + nk
        # 如果有ni=4,把4分成2+2，但对乘积没有影响
        # 如果有ni>5，分成3(ni-3)
        # 这样一来，我们就只剩下3 和 2了
        # 如果有三个2，把他们变成两个3
        # 所以我们尽可能拆出更多的3
        res = 1
        if n % 3 == 1:
            res *= 4
            n -= 4
        elif n % 3 == 2:
            res *= 2
            n -= 2
        while n:
            res *= 3
            n -= 3
        return res
        