class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return -1
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        #end_while
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1