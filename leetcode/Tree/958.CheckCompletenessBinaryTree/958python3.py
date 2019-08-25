# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getHeight(self, root) -> int:
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        maxth = self.getHeight(root)
        print(maxth)
        flag = False
        
        def check(root, h, maxth):
            nonlocal flag
            if h < maxth - 1:
                if not root.left or not root.right:
                    return False
            else:
                if not root.right and not root.left:
                    flag = True
                    return True
                elif not root.left and root.right:
                    return False
                elif not root.right and root.left:
                    if flag:
                        return False
                    flag = True
                    return True
                else:
                    if flag:
                        return False
                    return True
            if root:
                return check(root.left, h+1, maxth) and check(root.right, h+1, maxth)

            return False
        
        return check(root, 1, maxth)
        