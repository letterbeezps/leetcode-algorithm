# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return None
        
        return self.dfs(1, n)
    
    def dfs(self, l, r):
        res = []  #List[TreeNode]
        if l > r:
            res.append(None)
            return res
        
        for i in range(l, r+1):
            left = self.dfs(l, i-1)
            right = self.dfs(i+1, r)
            for item_l in left:
                for item_r in right:
                    root = TreeNode(i)
                    root.left = item_l
                    root.right = item_r
                    res.append(root)
        return res
        