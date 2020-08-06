# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        res = []
        
        def dfs(node):
            if node:
                uid = trees[node.val, dfs(node.left), dfs(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    res.append(node)
                return uid
        dfs(root)
        return res
        