'''
convert '0' to '-1'
-1,-1,-1,-1,1,1,1,-1,1
s += 1 if nums[i] else -1  hash[s]
hash[0] = -1
hash[-1] = 0
hash[-2] = 1
hash[-3] = 2  s = -3
hash[-4] = 3  s = -4
s = -3, i = 4 --> i - hash[-3] = 2 
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = collections.defaultdict(int)
        hash[0] = -1
        L = len(nums)
        s, res = 0, 0
        for i in range(L):
            s += 1 if nums[i] else -1
            if s in hash:
                res = max(res, i-hash[s])
            else:
                hash[s] = i  # 只统计它第一次出现的位置，
                             # 当它再次出现的时候，中间相隔的子序列就是潜在答案子序列
        #end_for
        return res