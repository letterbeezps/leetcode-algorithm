# _*_ coding: utf-8 _*
from BinaryTree import Tree, Node

"""
给定一个生序数组，构造一个平衡二叉搜索树BST（又名二叉排序树，或二叉查找树）
分析：因为已经给了一个生序数组，所以只要考虑在不破坏顺序的情况下构造二平衡二叉树
考虑把数组[1,n]分成[1,mid-1],[mid],[mid+1,n]，其中mid=[n/2]
"""

def SubTreeSlove(nums, l, r):
    mid = (l+r+1) // 2  # 取中间数的索引
    print(mid)
    node = Node(nums[mid])
    if mid > l:
        node.left = SubTreeSlove(nums, l, mid-1)
    if mid < r:
        node.right = SubTreeSlove(nums, mid+1, r)
    return node

def sortedArrayToBST(nums):
    T = Tree()
    if len(nums) == 0:
        return T
    else:
        T.root = SubTreeSlove(nums, 0, len(nums)-1)
    return T

nums = [-10, -3, 0, 5, 9]
T = sortedArrayToBST(nums)
print(T.preorder(T.root))
