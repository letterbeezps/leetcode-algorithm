class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        # dp[c]: num of tree rooted at c
        # dp[c] = sum{dp[a] * dp[b]} all c = a*b
        mod = 1000000007
        A.sort()
        dp = {}
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i]//A[j] in dp:
                    dp[A[i]] += (dp[A[j]] * dp[A[i] // A[j]]) % mod
        ans = 0
        for item in dp.values():
            ans += item
        return ans % mod
        