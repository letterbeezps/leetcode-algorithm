# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        def bfs(root):
            if not root: return -1
            s1 = root.val
            s2 = 2**32
            found = False
            q = collections.deque()  # TreeNode
            q.append(root)
            
            while q:
                node = q[0]
                q.popleft()
                if s1 < node.val < s2:
                    s2 = node.val
                    found = True  # 不需要考虑它的子节点来
                    continue
                if not node.left: continue
                q.append(node.left)
                q.append(node.right)
            return s2 if found else -1
        
        def dfs(root, s1):
            if not root: return -1
            
            if root.val > s1:
                return root.val
            sl = dfs(root.left, s1)
            sr = dfs(root.right, s1)
            if sl == -1: return sr
            if sr == -1: return sl
            
            return min(sl, sr)
        return dfs(root, root.val)
        
        
            
        # return bfs(root)
        