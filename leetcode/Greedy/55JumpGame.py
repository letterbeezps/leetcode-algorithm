class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 0  # 从第0为能跳到最远的距离
        i = 0
        while i < len(nums) and i <= dist:
            dist = max(dist, nums[i] + i)
            i += 1
        return dist >= len(nums)-1
        