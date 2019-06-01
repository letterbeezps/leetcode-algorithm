'''
inorder   : 9 3 15 20 7
            l1 m      r1
postorder : 9 15 7 20 3
            l2        r2
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        if n == 0: return None
        
        dict = {}
        for i in range(n):
            dict[inorder[i]] = i  # 中序遍历 值与下标
            
        def dfs(l1, r1, l2, r2, inorder: List[int], postorder: List[int], dict):
            if r1 >= l1 and r2 >= l2:
                root = TreeNode(postorder[r2])
                mid = dict[root.val]
                lsize = mid - l1
                rsize = r1 - mid
                root.left = dfs(l1, l1+lsize-1, l2, l2+lsize-1, inorder, postorder, dict)
                root.right = dfs(mid+1, r1, l2+lsize, r2-1, inorder, postorder, dict)
                return root
        
        root = dfs(0, n-1, 0, n-1, inorder, postorder, dict)
        return root
        
        