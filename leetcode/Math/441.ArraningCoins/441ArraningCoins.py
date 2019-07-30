class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, q = 0, n
        ans = 0
        while q > i:
            ans += 1
            i += 1
            q -= i
        return ans
        