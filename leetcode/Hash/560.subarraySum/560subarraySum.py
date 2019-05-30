'''
k = c+d
[a,b,c,d,e,f,g]
s0=0
s1=a
s2=a+b
s3=a+b+c
s4=a+b+c+d
s5=a+b+c+d+e
s4 - s2 = k
s4出现时，s2的次数就是答案之一
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = collections.defaultdict(int)
        hash[0] = 1  # 若k等于a+b，那就要统计s0的次数，且初始值为1
        res, s = 0, 0
        for x in nums:
            s += x
            res += hash[s - k]
            hash[s] += 1
        return res