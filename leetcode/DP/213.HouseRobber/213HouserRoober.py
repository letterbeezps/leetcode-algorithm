class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        if len(nums) == 4:
            return max(nums[0]+nums[2], nums[1]+nums[3])
        n = len(nums)
        
        f = [0] * n
        num1 = nums[:-1]
        f[1] = num1[0]
        for i in range(2, n):
            f[i] = max(f[i-2]+num1[i-1], f[i-1])
        temp1 = f[n-1]
        
        f = [0] * n
        num2 = nums[1:]
        f[1] = num2[0]
        for i in range(2, n):
            f[i] = max(f[i-2]+num2[i-1], f[i-1])
            
        temp2 = f[n-1]
        
        return max(temp1, temp2)