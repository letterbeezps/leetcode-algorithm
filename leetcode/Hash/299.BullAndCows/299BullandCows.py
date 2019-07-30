class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        n = len(guess)
        ds = [0] * 10
        dg = [0] * 10
        for i in range(n):
            x, y = int(secret[i]), int(guess[i])
            if x == y:
                a += 1
            ds[x] += 1
            dg[y] += 1
        
        for i in range(10):
            b += min(ds[i], dg[i])
        b -= a
        return str(a)+'A'+str(b)+'B'