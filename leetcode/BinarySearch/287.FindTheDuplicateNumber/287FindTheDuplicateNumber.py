class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        # mid = left + (right - left) // 2
        while left < right:
            count = 0
            mid = left + (right - left) // 2
            for x in nums:
                if x <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid+1
        return left
            