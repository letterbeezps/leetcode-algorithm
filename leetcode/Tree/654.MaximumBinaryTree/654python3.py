class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        index = nums.index(max(nums))
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root


###################Solution 2################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        stack = []
        stack.append(TreeNode(nums[0]))
        root = stack[0]
        for num in nums[1:]:
            node = TreeNode(num)
            if node.val < stack[-1].val:
                stack[-1].right = node
                stack.append(node)
                continue
            while stack and node.val > stack[-1].val:
                stack.pop()
            if stack:
                temp = stack[-1].right
                stack[-1].right = node
                node.left = temp
            else:
                node.left = root
                root = node
            stack.append(node)
        return root
                          