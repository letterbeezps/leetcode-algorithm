class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 相邻相同元素-->合并
        # groupby把相邻的重复元素挑出来放在一起
        new_nums = [k for k, g in itertools.groupby(nums)]
        
        L = len(new_nums)
        if L <= 2:
            return L
        res = 2
        for i in range(1, L-1):
            a = new_nums[i-1]
            b = new_nums[i]
            c = new_nums[i+1]
            # 找局部最大值/最小值
            if a < b > c:
                res += 1
            elif a > b < c:
                res += 1
        #end_for
        return res