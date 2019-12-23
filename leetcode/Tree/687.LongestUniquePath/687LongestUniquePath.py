# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root)
        return self.result
        
        
    def dfs(self, node: TreeNode):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        leftPath = left+1 if node.left and node.left.val == node.val else 0
        rightPath = right+1 if node.right and node.right.val == node.val else 0
        
        self.result = max(self.result, leftPath+rightPath)
        return max(leftPath, rightPath)