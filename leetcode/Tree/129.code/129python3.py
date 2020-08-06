# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        path = ''
        def dfs(root, path):
            if not root:
                return
            nonlocal ans
            path += str(root.val)
            if not root.left and not root.right:
                ans += int(path)
                return
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, path)
        return ans