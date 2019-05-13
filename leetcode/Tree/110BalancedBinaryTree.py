# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def Height(root: TreeNode):
            if root == None:
                return 0
            left = Height(root.left)
            right = Height(root.right)
            
            if left<0 or right <0 or abs(left-right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return Height(root) >= 0 