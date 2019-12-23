class NumArray:
    
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sumn = [0] * (n+1)  # 前缀和，习惯下标从1开始
        for i,num in enumerate(nums):
            self.sumn[i+1] = self.sumn[i] + num    
        

    def sumRange(self, i: int, j: int) -> int:
        return self.sumn[j+1] - self.sumn[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)