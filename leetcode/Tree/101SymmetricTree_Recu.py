# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(left: TreeNode, right: TreeNode):
            if left and right:
                return left.val == right.val and isSame(left.left, right.right) and isSame(left.right, right.left)
            return left == right
        
        if not root:
            return True  # 空节点一定对称
        return isSame(root.left, root.right)
        