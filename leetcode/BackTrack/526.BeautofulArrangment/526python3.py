class Solution:
    def countArrangement(self, N: int) -> int:
        f = [0] * (1 << N)
        f[0] = 1
        for i in range(1 << N):
            s = 1
            for j in range(N):
                s += i >> j & 1
            for j in range(1, N+1):
                tag = j % s == 0 or s % j == 0
                if not(i >> (j-1) & 1) and tag:
                    f[i | (1 << j-1)] += f[i]
        return f[(1 << N) - 1]
                