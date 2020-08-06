# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        s = str(t.val)
        l = self.tree2str(t.left)
        r = self.tree2str(t.right)
        if not t.left and not t.right:
            return s
        if not t.right:
            return s + '(' + l + ')'
        # general case
        return s + '(' + l + ')' + '(' + r + ')'
        