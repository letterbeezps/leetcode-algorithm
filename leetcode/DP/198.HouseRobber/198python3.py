class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        f = [0] * (n+1)
        f[1] = nums[0]
        for i in range(2, n+1):
            f[i] = max((f[i-2]+nums[i-1]), f[i-1])
        return f[n]