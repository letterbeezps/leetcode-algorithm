class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        total, res = 0, 0
        for i in range(n-1):
            total += abs(nums[i] - nums[i+1])
            
        for i in range(1, n):
            res = max(res, abs(nums[0]-nums[i]) - abs(nums[i-1]-nums[i]))
        for i in range(n-1):
            res = max(res, abs(nums[n-1]-nums[i]) - abs(nums[i+1]-nums[i]))
            
        if n <= 3:
            return total+res
        
        x = max(nums[0], nums[1])
        
        for i in range(2, n-1):
            m = min(nums[i], nums[i+1])
            if m > x:
                res = max(res, 2*(m-x))
            x = min(x, max(nums[i-1], nums[i]))
            
        x = max(nums[n-1], nums[n-2])
        for i in range(n-3, 0, -1):
            m = min(nums[i], nums[i-1])
            if m > x:
                res = max(res, 2*(m-x))
            x = min(x, max(nums[i], nums[i+1]))
        return total+res