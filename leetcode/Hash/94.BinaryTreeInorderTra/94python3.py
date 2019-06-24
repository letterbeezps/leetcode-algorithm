# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return res
        

##########################################
#################solution2################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []  # stack<pair<TreeNode*, int>>
        stack.append([root, 0])  # 0表示还没遍历该节点的左子树
        while stack:
            if not stack[-1][0]:
                stack.pop()
                continue
            
            t = stack[-1][1]
            if t == 0:
                stack[-1][1] = 1 # 遍历它的左子树
                stack.append([stack[-1][0].left, 0])  # 左子树入栈
            elif t == 1:  # 左子树已经遍历完
                res.append(stack[-1][0].val)   # 遍历中间节点
                stack[-1][1] = 2
                stack.append([stack[-1][0].right, 0])  # 右子树入栈
            else:
                stack.pop()
        #end_while
        return res
        