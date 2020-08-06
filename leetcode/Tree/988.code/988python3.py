# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""
        self.ans = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        path = ""

        def dfs(root, path):
            if not root:
                return
            path += chr(97+root.val) # 梅西该操作是新建一个字符串，不同于列表
            if not root.left and not root.right:
                self.ans = min(self.ans, path[::-1])
                return
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, path)
        return self.ans
            