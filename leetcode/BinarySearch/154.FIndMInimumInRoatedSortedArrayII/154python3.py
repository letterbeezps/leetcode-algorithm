'''
参考第153题，
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0],nums[-1])
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        minm = nums[0]
        while left <= right:
            mid = left + (right-left) // 2
            if mid > 0 and mid+1 < len(nums) and nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            elif left > 0 and left+1 < len(nums) and nums[left-1] > nums[left] < nums[left+1]:
                return nums[left]
            elif right > 0 and right+1 < len(nums) and nums[right-1] > nums[right] < nums[right+1]:
                return nums[right]
            elif nums[mid] > nums[0]:
                if nums[mid] < minm:
                    minm = nums[mid]
                left = mid+1
                
            elif nums[mid] < nums[0]:
                if nums[mid] < minm:
                    minm = nums[mid]
                right = mid-1
                
            else:
                if nums[mid] < minm:
                    minm = nums[mid]
                left += 1
                
        print(left)
        print(right)
        #end_while
        # return min(nums[left], nums[right])
        min1, min2 = nums[1], min(nums[-1], nums[-2])
        
        return min(min1, min2, minm)
        # return nums[-1]
        
        