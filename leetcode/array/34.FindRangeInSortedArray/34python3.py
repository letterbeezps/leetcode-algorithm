'''
XXXXXX ttttt yyyyyy
if [mid] != t : Binary S
if [mid] == t :
    find start
        right = mid
    find end
        left = mid
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not len(nums):
            return res
        s_point, e_point = -1, -1
        left, right = 0, len(nums)-1
        while left < right:
            # find the s_point
            mid = left + right >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        #end_while
        if nums[left] == target:
            s_point = left
        if s_point == -1:
            return res
        
        left, right = 0, len(nums)-1
        while left < right:
            # find the e_point
            mid = left + right + 1 >> 1
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid
        #end_while
        e_point = left
        res = [s_point, e_point]
        return res
        