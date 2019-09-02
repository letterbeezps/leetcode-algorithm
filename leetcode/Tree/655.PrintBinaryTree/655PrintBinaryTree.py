# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# h
# w = 2 ** h - 1
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        h = self.getHeight(root)
        w = (1 << h) - 1
        res = [[""] * w for _ in range(h)]
        self.fill(root, res, 0, 0, w-1)
        
        return res
    
    def getHeight(self, root: TreeNode):
        if not root:
            return 0
        
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
    def fill(self, root, res: list, h: int, l, r):
        if not root:
            return
        mid = (l + r) // 2
        res[h][mid] = str(root.val)
        self.fill(root.left, res, h+1, l, mid-1)
        self.fill(root.right, res, h+1, mid+1, r)
        