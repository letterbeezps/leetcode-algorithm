# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.maxSum = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathSumRoot(root)
        
        return self.maxSum
        
    def maxPathSumRoot(self, root):
        if not root:
            return 0
        
        left = self.maxPathSumRoot(root.left)
        right = self.maxPathSumRoot(root.right)
        
        self.maxSum = max(max(left,0)+max(right,0)+root.val, self.maxSum)
        
        return max(left, right, 0) + root.val
        