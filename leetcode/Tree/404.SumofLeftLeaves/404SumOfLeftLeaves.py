# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        sumn = 0
        if root.left and not root.left.left and not root.left.right:
            sumn = root.left.val
        return sumn + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)