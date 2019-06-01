class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []  #vetor<vector<int>>
        path = []  # vector<int>
        st = [False] * len(nums)  # vector<bool>
        
        def dfs(nums: List[int], u: int):
            if u == len(nums):
                path1 = path + []
                ans.append(path1)
                return
            for i in range(len(nums)):
                if not st[i]:
                    st[i] = True
                    path.append(nums[i])
                    dfs(nums, u+1)
                    st[i] = False
                    path.pop()
        
        dfs(nums, 0)
        return ans
        
       
                    