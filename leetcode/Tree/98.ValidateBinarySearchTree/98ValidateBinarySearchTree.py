# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(node, minval = -float('inf'), maxval = float('inf')) -> bool:
            if not node:
                return True
            if not minval < node.val < maxval:
                return False
            return helper(node.left, minval, node.val) and helper(node.right, node.val, maxval)
        
        return helper(root)
                