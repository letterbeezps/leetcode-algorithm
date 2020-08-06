class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        
        def dfs(nums, lst, pos):

            res.append(lst[:])
            for i in range(pos, len(nums)):
                lst.append(nums[i])
                dfs(nums, lst, i+1)
                lst.pop()
            
        dfs(nums, [], 0)
        return res
        