# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
        
    def dfs(self, root):
        if not root:
            return -1
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1
        
        self.ans = max(self.ans, left+right)
        
        return max(left, right)