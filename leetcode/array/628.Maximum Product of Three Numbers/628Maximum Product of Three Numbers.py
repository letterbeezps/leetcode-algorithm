class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        
        return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])
        