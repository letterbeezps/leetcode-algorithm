# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def order_sum(self, root: TreeNode):
        if not root:
            return 0
        if root in self.temp:
            return self.temp[root]
        self.temp[root] = root.val + self.order_sum(root.left) + self.order_sum(root.right)
        return root.val + self.order_sum(root.left) + self.order_sum(root.right)
        
    
    def maxProduct(self, root: TreeNode) -> int:
        self.temp = {}
        all_sum = self.order_sum(root)  # 先做一个记忆化存储，每个节点为根结点的子树全部节点之和
        model = 1e9+7
        
        split_root = []
        self.split(root, split_root)
        
        res = []
        for item in split_root:
            res.append(item * (all_sum-item))
        return int(max(res) % model)
        
        
    def split(self, root, split_root):
        if not root:
            return
        split_root.append(self.temp[root])
        self.split(root.left, split_root)
        self.split(root.right, split_root)
        
        
        