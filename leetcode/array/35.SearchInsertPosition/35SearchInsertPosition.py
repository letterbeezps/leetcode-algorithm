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
        while left+1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        #end_while
        if nums[right] < target:
            return right+1
        elif nums[left] >= target:
            return left
        else:
            return right