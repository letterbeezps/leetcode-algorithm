# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
   3           level = [3]----->|
   / \                          |
  9  20    |<--level = [9,20]<--|
    /  \   |
   15   7  |-->level = [15,7]-->
   参看102题，小修改
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        def get_val(level: List[TreeNode]): # level is List[TreeNode]
            res = []
            for x in level:
                res.append(x.val)
            return res
        
        res = [] # List[List[]]
        tar = 0  # 0 means right
        if not root:
            return res
        level = [] # List[TreeNode]
        level.append(root)
        res.append(get_val(level))
        
        while True:
            newlevel = []
            if tar:
                for x in level:
                    if x.left:
                        newlevel.append(x.left)
                    if x.right:
                        newlevel.append(x.right)
            else:
                for x in level:
                    if x.right:
                        newlevel.append(x.right)
                    if x.left:
                        newlevel.append(x.left)                
            tar = (tar+1) % 2
            if len(newlevel):
                res.append(get_val(newlevel))
                newlevel.reverse()
                level = newlevel
            else:
                break
        #end_while
        return res
        