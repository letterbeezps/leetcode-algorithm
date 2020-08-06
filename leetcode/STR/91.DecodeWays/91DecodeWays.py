class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * (n+1)
        s = ' ' + s
        f[0] = 1
        for i in range(1, n+1):
            f[i] = 0
            if s[i] != '0':
                f[i] += f[i-1]
            if i > 1:
                t = int(s[i-1]) * 10 + int(s[i])
                if 10 <= t <= 26:  # for the case '01', t is <=10, and t can not be decoded
                    f[i] += f[i-2]
                    
        # endfor
        return f[n]