# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        s1 = []
        s2 = []
        res = []
        self.traverse(root1, s1)
        self.traverse(root2, s2)
        i = j = 0
        while i<len(s1) or j<len(s2):
            if j==len(s2):
                res.append(s1[i])
                i += 1
            elif i==len(s1):
                res.append(s2[j])
                j += 1
            else:
                if s1[i] < s2[j]:
                    res.append(s1[i])
                    i += 1
                else:
                    res.append(s2[j])
                    j += 1
        return res
        
    def traverse(self, root, s: list):
        if not root:
            return
        self.traverse(root.left, s)
        s.append(root.val)
        self.traverse(root.right, s)
    
        