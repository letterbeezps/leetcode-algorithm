# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# left = 左子树节点的个数
# k <= left: dfs(root.left, k)
# k = left + 1: return root
# k > left + 1: return dfs(root.right, k-left-1)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        K = [k]  # 使用列表是因为python函数参数的变量具有不变性，如果是可迭代对象则直接传引用
        return self.dfs(root, K)
        
    
    def dfs(self, root: TreeNode, K):
        if not root:
            return 0;
        left = self.dfs(root.left, K)
        if K[0]<=0:
            return left
        K[0] -= 1
        if K[0] == 0:
            return root.val
        
        return self.dfs(root.right, K)
        