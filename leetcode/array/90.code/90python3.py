class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()

        ans = []
        n = len(nums)
        def dfs(nums, lst: List, pos):
            preNum = '#'
            ans.append(lst[:])
            for i in range(pos, n):
                if nums[i] != preNum:
                    preNum = nums[i]
                    lst.append(nums[i])
                    dfs(nums, lst, i+1)
                    lst.pop()
        dfs(nums, [], 0)
        return ans