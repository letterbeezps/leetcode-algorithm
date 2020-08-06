class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not len(nums):
            return nums
        m,n = len(nums), len(nums[0])
        
        if m*n != r*c:
            return nums
        
        res = [[0] * c for _ in range(r)]
        
        for i in range(m*n):
            org_x = i // n
            org_y = i % n
            new_x = i // c
            new_y = i % c
            res[new_x][new_y] = nums[org_x][org_y]
            
        return res
        