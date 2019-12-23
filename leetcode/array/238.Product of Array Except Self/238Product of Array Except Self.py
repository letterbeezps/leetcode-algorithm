# res[i] = nums[0]   i-1 * i+1,  n
# 先前向累乘法， 再后向累乘
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 不用乘法
        res = [0] * len(nums)
        t = 1
        for i in range(len(nums)):
            res[i] = t
            t *= nums[i]
        # print(res)
        t = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= t
            t *= nums[i]
        return res