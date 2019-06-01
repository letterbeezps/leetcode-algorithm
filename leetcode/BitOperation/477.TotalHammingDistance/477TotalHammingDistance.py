'''
假设有四个数
1111
1110
1101
1100
先看他们第一位上的汉明距离，取每个数的第一位
1 0 1 0  相同距离为0，不同距离为0
本质就是从{1,1} {0,0}各取一个数，他们距离为1，共有4种取法
对应到其它位上同理
'''
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        L = len(nums)
        for i in range(30):
            ones = 0
            for x in nums:
                if x >> i & 1:
                    ones += 1
            #end_for
            res += ones * (L-ones)
        #end_for
        return res