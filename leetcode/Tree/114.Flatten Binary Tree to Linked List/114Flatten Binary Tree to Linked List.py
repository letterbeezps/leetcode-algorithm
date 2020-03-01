# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if root.left:
            temp = root.left
            while temp.right:
                temp = temp.right
            temp.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right)
        