# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        l, r = 0, 0
        l_, r_ = 0, 0
        def nodes(root: TreeNode, x: int):
            if not root:
                return 0
            l = nodes(root.left, x)
            r = nodes(root.right, x)
            nonlocal l_, r_
            if root.val == x:
                l_ = l
                r_ = r
                
            return 1+l+r
        nodes(root, x)
        p = n - 1 - l_ - r_
        return max(p, max(l_, r_)) > n // 2
            