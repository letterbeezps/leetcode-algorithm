# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        #题意，把一棵树的中序遍历结果建成一颗新的树
        s = []
        dummy = TreeNode(0)
        p = dummy
        
        while s or root:
            if root:
                #中序遍历，先把左孩子进栈
                s.append(root)
                root = root.left
            else:
                cur = s.pop()
                root = cur.right
                cur.left = None
                p.right = cur
                p = p.right
        return dummy.right