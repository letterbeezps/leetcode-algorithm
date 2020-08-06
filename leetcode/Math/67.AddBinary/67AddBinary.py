class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]  # first step, reverse str
        carry, res = 0, []
        length = max(len(a), len(b))
        for i in range(length):
            curra = 0 if i >= len(a) else int(a[i])
            currb = 0 if i >= len(b) else int(b[i])
            s = curra + currb + carry
            carry = s // 2
            s %= 2
            res.append(str(s))
        if carry:
            res.append('1')
        return ''.join(res[::-1])