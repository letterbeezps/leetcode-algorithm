# 前缀合
# s[i] - S = s[j]
# 我们要求有多少种i, j组合满足s[i] - S = s[j]
# 问题变成给定sumn[i],有多少个j使得sumn[j] = s[i] - S
# f[i]表示sumn[]有多少个数的值是i
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        # sumn[i] = A[0] +... + A[i-1]
        sumn = [0] * (n+1)
        f = [0] * (n+1)  # f[i]表示sumn[]有多少个数的值是i
        
        for i,a in enumerate(A):
            sumn[i+1] = sumn[i] + A[i]
            
        f[0] = 1  # sumn[0] = 0，这是已知的
        
        res = 0
        for i in range(1, n+1):
            if sumn[i] - S >= 0:
                res += f[sumn[i] - S]
            f[sumn[i]] += 1
        return res