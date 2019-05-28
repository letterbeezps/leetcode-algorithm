'''
先求出总和，若总和不能被4整除，直接false
除以4后得到正方形的边长
再建立一个数组subsum[4]用来记录在dfs中累加的四条边长，
每条边可以由一个或多个火柴组成，但是每条边最后的长度必须相等
否则就无法构成正方形
'''
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        Circum = 0
        for x in nums:
            Circum += x
        l = Circum // 4
        if l * 4 != Circum:
            return False
        
        nums.sort(key=lambda x: -x)
        Subsum = [0] * 4
        
        def dfs(nums, Subsum, length: int, index: int):
            if Subsum[0] == length and Subsum[1] == length and Subsum[2] == length:
                return True
            for i in range(4):
                if Subsum[i] + nums[index] > length:
                    continue
                Subsum[i] += nums[index]
                if dfs(nums, Subsum, length, index+1):
                    return True
                Subsum[i] -= nums[index]
            return False
                
        res = dfs(nums, Subsum, l, 0)
        return res