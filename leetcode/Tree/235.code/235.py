# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        def dfs(root, p, q):
            # p.val <= q.val
            if not root:
                return None
            if p.val <= root.val <= q.val:
                return root
            elif root.val < p.val:
                return dfs(root.right, p, q)
            else:
                return dfs(root.left, p, q)
        if p.val <= q.val:
            return dfs(root, p, q)
        else:
            return dfs(root, q, p)