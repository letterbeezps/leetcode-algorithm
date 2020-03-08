class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 前缀和
        n = len(nums)
        s = [0] * (n+1)
        
        for i in range(n):
            s[i+1] = s[i] + nums[i]
        for i in range(1, n+1):
            if s[i-1] == s[-1] - s[i]:
                return i-1
        return -1
        