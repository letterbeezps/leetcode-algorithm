class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        python list 里还没找到原地给列表部分排序，
        numpy的array可以原地部分排序
        """
        
        if not nums:
            return
        replace = len(nums)-2
        while replace >= 0:
            # 找到第一个逆序
            if nums[replace] < nums[replace+1]:
                break
            replace -= 1
        #end_while
        if replace < 0:
            nums.sort()
            return
        # 寻找和replace呼唤的值
        lgIndx = replace + 1
        while lgIndx < len(nums) and nums[lgIndx] > nums[replace]:
            lgIndx += 1
        
        nums[replace], nums[lgIndx-1] = nums[lgIndx-1], nums[replace]
        # 这不是真正的原地排序
        nums[replace+1: len(nums)] = sorted(nums[replace+1: len(nums)])