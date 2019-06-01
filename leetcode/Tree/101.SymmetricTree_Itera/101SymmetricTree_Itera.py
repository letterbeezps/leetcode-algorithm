# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2:  # 为空，判断对称
                continue
            if not t1 or not t2:
                return False       # 一个子节点为空
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        #end_while
        return True