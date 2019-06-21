class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            elif nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < nums[right]:
                if nums[mid] < target < nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                left += 1
        #end_while
        if nums[left] == target or nums[right] == target:
            return True
        else:
            return False
        