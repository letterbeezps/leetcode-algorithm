class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        res = 0
        i = 0
        while i<len(nums):
            res += nums[i]
            i += 2
            
        return res