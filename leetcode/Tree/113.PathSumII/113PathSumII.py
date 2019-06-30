# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sumn: int) -> List[List[int]]:
        if not root:
            return []
        res, path = [], []
        
        def dfs(u: TreeNode, sumn):
            if not u:
                return
            path.append(u.val)
            if not u.left and not u.right:
                if sumn == u.val:
                    path1 = path + []
                    res.append(path1)
            dfs(u.left, sumn-u.val)
            dfs(u.right, sumn-u.val)
            path.pop()
        dfs(root, sumn)
        return res
                
        