class Solution:
    def combinationSum(self, candi: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        if not candi:
            return res
        candi.sort()
        
        def dfs(candi: List[int], target, index, res, path):
            if target == 0:
                path1 = path + []
                res.append(path1)
            elif target > 0:
                for i in range(index, len(candi)):
                    if candi[i] > target:
                        break
                    path.append(candi[i])
                    print(path)
                    dfs(candi, target-candi[i], i, res, path)
                    path.pop()
        #end
        dfs(candi, target, 0, res, path)
        return res