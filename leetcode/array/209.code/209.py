class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s > sum(nums):
            return 0
        l, r = 0, 0
        ans = len(nums)+1
        while r < len(nums):
            if sum(nums[l:r+1]) <s:
                r += 1
            if sum(nums[l:r+1]) >=s:
                ans = min(ans, r-l+1)
                l += 1
        return ans