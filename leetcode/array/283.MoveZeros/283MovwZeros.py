class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = 0
        for post in range(len(nums)):
            if nums[post]:
                nums[pre] = nums[post]
                pre += 1
        nums[pre:] = [0] * (len(nums)-pre)
        