"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        level = [root]
        while True:
            newlevel = []
            for i, node in enumerate(level):
                if i < len(level)-1:
                    level[i].next = level[i+1]
                # print(node.val, end=' ')
                if node.left:
                    newlevel.append(node.left)
                    newlevel.append(node.right)
            if newlevel:
                level = newlevel
            else:
                break

        return root
