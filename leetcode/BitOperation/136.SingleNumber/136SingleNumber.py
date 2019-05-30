'''
重复出现的数做异或运算就会变成 00000000......的形式
而对0000000......做异或本身保持不变
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        #end_for
        return res