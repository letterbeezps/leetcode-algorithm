class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        x = nums[n//2]
        
        res = 0
        for num in nums:
            res += abs(x-num)
        return res