# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
BFS: 空间是指数级别的
     不会爆栈
     最短，最小
DFS: 空间和深度成正比
     有爆栈的风险，假如树有10w层
     不能搜最短，最小
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left or not right:
            return left+right+1
        else:
            return min(left, right)+1