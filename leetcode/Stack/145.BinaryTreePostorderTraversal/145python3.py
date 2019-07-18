# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = collections.deque()
        s = []  # stack
        s.append(root)
        while s:
            node = s.pop()
            ans.appendleft(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return list(ans)