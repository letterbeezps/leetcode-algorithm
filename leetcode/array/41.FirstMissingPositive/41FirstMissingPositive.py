class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 2**31-1
        
        for i in range(len(nums)):
            num = abs(nums[i])
            if num <= len(nums):
                nums[num-1] = -abs(nums[num-1])
                
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
            
        return len(nums)+1
        