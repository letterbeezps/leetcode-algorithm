class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l = len(nums)
        if nums[0] > target:
            return 0
        elif nums[l-1] < target:
            return l
        # binary search
        left = 0
        right = l-1
        while left < right:
            mid = left + right >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
                