# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
参考102，小修改
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def get_val(level: List[TreeNode]): # level is List[TreeNode]
            res = []
            for x in level:
                res.append(x.val)
            return res
        
        res = [] # List[List[]]
        if not root:
            return res
        level = [] # List[TreeNode]
        level.append(root)
        res.append(get_val(level))
        
        while True:
            newlevel = []
            for x in level:
                if x.left:
                    newlevel.append(x.left)
                if x.right:
                    newlevel.append(x.right)
            if len(newlevel):
                res.append(get_val(newlevel))
                level = newlevel
            else:
                break
        #end_while
        res.reverse()
        return res