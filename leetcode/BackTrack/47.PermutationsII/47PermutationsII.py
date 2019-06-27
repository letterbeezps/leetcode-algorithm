class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []  #vetor<vector<int>>
        path = []  # vector<int>
        st = [False] * len(nums)  # vector<bool>
        nums.sort()
        
        def dfs(nums: List[int], u: int):
            if u == len(nums):
                path1 = path + []
                ans.append(path1)
                return
            preNum = nums[0] - 1
            for i in range(len(nums)):
                if not st[i] and nums[i] != preNum:
                    preNum = nums[i]
                    st[i] = True
                    path.append(nums[i])
                    dfs(nums, u+1)  # 你的preNum和你的上一层dfs的preNum性质不一样
                    st[i] = False
                    path.pop()
        
        dfs(nums, 0)
        return ans