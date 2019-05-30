# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, l1, r1, l2, r2, preorder, inorder, dict):
        """
        """
        if r1 >= l1 and r2 >= l2:
            root = TreeNode(preorder[l1])
            mid = dict[root.val] #找到根节点在中序里的位置
            #print(mid)
            lsize = mid - l2
            rsize = r2 - mid    #找到两个子树的范围
            root.left = self.dfs(l1+1, l1+lsize, l2, l2+lsize-1, preorder, inorder, dict)
            root.right = self.dfs(l1+lsize+1, l1+lsize+rsize, mid+1, mid+rsize, preorder, inorder, dict)
            #print(root.val)
            return root
        
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict = {}
        n = len(preorder)
        if n == 0:
            return None
        for i in range(n):
            dict[inorder[i]] = i
        
        root = self.dfs(0, n-1, 0, n-1, preorder, inorder, dict)
        return root