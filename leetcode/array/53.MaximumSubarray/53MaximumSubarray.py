######################solution  dynamic programming############
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxn, max_curr = nums[0], nums[0]
        for x in nums[1:]:
            max_curr = max(max_curr+x, x )
            maxn = max(maxn, max_curr)
        return maxn


#############solution divide and conquer
class Solution:
    # divide and conquer: compute the maximum value of the left and right side separately
    # and don't the maximum across the middle
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def MaxCross(nums, low, mid, high):
            left_sum, sumn = -2147483648, 0
            for i in range(mid, low-1, -1):
                sumn += nums[i]
                if sumn > left_sum:
                    left_sum = sumn
                    max_left = i
            right_sum, sumn = -2147483648, 0
            for i in range(mid+1, high+1):
                sumn += nums[i]
                if sumn > right_sum:
                    right_sum = sumn
                    max_right = i
            return left_sum+right_sum
        
        def MAXMUM(nums, low, high) -> int:
            if low == high:
                return nums[low]
            mid = low + (high-low) // 2
            left_sum = MAXMUM(nums, low, mid)
            right_sum = MAXMUM(nums, mid+1, high)
            cross_sum = MaxCross(nums, low, mid, high)
            return max(left_sum, right_sum, cross_sum)
        
        return MAXMUM(nums, 0, len(nums)-1)
'''
'''
