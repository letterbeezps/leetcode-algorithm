# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
DP
对于第i个节点只有拿与不拿两种情况，给出以i位根节点的子树
f[i][0]  在i不行窃的最大收益
f[i][1]  在i行窃的最大收益

若在i行窃，那么在i.left & i.right 不行窃
反之，在i节点的收益是两个子节点收益的最大值
'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        f = collections.defaultdict(list) # key: TreeNode  value:  list[int]
    
        def dfs(root: TreeNode):
            f[root] = [0,0]
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            f[root][1] = root.val + f[root.left][0] + f[root.right][0]
            f[root][0] = max(f[root.left][0], f[root.left][1]) + max(f[root.right][0], f[root.right][1])
            
        dfs(root)
        return max(f[root][0], f[root][1])