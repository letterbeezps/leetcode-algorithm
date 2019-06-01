class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        k1 = l - k
        if k != 0:
            for i in range((k1 - 1) // 2 + 1):
                t1 = nums[i]
                nums[i] = nums[k1 - 1 - i]
                nums[k1 - 1 - i] = t1
            for j in range(k1,(k1 + l - 1) // 2 + 1):
                t2 = nums[j]
                nums[j] = nums[l - 1 + k1 - j]
                nums[l - 1 + k1 - j] = t2
            nums.reverse()
                
            