'''
1 1 1 2 2 5567
1     2   5
  1   2   5
    1 2   5
这里开头有三个1（不同的1）假如125是答案之一
按照39题的思路，会生成三对 125
所以和39题相比，关键在于，相同的数，作为答案开头，只能出现一次，每次只选重复数字里的第一个数作为开头
注意：并不是答案里每个数字唯一，而是相同的数字不能发挥同样的作用
比如target=3， 答案1 1 1，这三个数的目标target的分别是3 2 1，它们的作用不一样
而target=8  ， 1 2 5，里面1 的目标target就是8
'''
class Solution:
    def combinationSum2(self, candi: List[int], target: int) -> List[List[int]]:
        path, res = [], []
        if not candi:
            return res
        candi.sort()
        
        def dfs(candi, target, index, res, path):
            if target == 0:
                path1 = path+[]
                res.append(path1)
            elif target > 0 and index < len(candi):
                for i in range(index+1, len(candi)):
                    if candi[i] > target:
                        break
                    if candi[i] != candi[index]:  # 找到下一层与当前不同的数字
                        dfs(candi, target, i, res, path)
                        break
                        
                path.append(candi[index])
                dfs(candi, target-candi[index], index+1, res, path)
                path.pop()
        dfs(candi, target, 0, res, path)
        return res