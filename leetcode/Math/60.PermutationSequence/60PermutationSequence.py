'''
关键在本题是要求all of the permutations is in order 分区考虑：
以123为例子，能分三个区
1 2 3
1 3 2

2 1 3
2 3 1

3 1 2
3 2 1
第k个数肯定在某一个区间，如k=4在第二个区间，而且是是第二个区间的第2个数
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = [''] * n
        nums = [i for i in range(1, n+1)]
        factorial = [0] * n
        factorial[0] = 1
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i
            
        k -= 1
        for i in range(n):
            res[i] = str(nums.pop(k // factorial[n-1-i]))
            k %= factorial[n-1-i]
            
        return ''.join(res)