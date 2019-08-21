'''
参考第33题，注意处理一下边界
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            #print(nums[-1])
            return nums[0]
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = left + (right-left) // 2
            if nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        #print(left)
        #print(right)
        #end_while
        if left > 0 and left+1 < len(nums) and nums[left-1] > nums[left] < nums[left+1]:
            return nums[left]
        if right > 0 and right+1 < len(nums) and nums[right-1] > nums[right] < nums[right+1]:
            return nums[right]
        return nums[-1]
        
## Solution 2##
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums)-1
        while l < r:
            mid = l+r >> 1
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]