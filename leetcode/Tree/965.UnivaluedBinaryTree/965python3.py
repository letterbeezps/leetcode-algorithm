#################solution1##############
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # 遍历整个树
        vals = lambda n: vals(n.left) + [n.val] + vals(n.right) if n else []
        return len(set(vals(root))) == 1


#################solution2##############
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.value = root.val
        
        def check(root: TreeNode):
            if not root:
                return True
            if self.value != root.val:
                return False
            return check(root.left) and check(root.right)
        
        return check(root)
        