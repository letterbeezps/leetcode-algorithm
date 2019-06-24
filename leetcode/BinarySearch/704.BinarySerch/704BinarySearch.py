class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
                
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        