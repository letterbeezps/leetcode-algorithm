class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return 0
        f = [1] * n
        f[0] = f[1] = 0
        for i in range(2, int(n**0.5)+1):
            if not f[i]:
                continue
            j = i*i
            while j<n:
                f[j] = 0
                j += i
        ans = sum(f)
        return ans
        