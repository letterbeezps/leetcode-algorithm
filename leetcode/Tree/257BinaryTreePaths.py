# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        path = ""
        self.dfs(root, path)
        return self.res
    
    def dfs(self, root, path):
        if not root:
            return
        if path != "":
            path += "->"
        path += str(root.val)
        if not root.left and not root.right:
            self.res.append(path)
        else:
            self.dfs(root.left, path)
            self.dfs(root.right, path)