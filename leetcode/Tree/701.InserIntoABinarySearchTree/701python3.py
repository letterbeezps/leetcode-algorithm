# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        pos = root
        t_parent = None
        while pos:
            t_parent = pos
            if val < pos.val:
                pos = pos.left
            else:
                pos = pos.right
        # figure the insert position
        if val < t_parent.val:
            t_parent.left = TreeNode(val)
        else:
            t_parent.right = TreeNode(val)
        return root
        