"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.ans = []
        
    def postorder(self, root: 'Node') -> List[int]:
        self.postorder_help(root)
        return self.ans
    
    def postorder_help(self, root: 'Node') -> List[int]:
        if not root:
            return 
        if root.children:
            for node in root.children:
                self.postorder_help(node)
        self.ans.append(root.val)