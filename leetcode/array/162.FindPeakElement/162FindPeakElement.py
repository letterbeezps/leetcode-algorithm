# key words nums[-1] = nums[n] = -inf
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        l, r = 1, len(nums)-1
        while l < r:
            mid = l+r+1 >> 1
            if nums[mid] > nums[mid-1]:
                l = mid
            else:
                r = mid - 1
        return l
        