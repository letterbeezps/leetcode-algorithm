# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
使用快慢指针找到中间节点
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # slow and fast
        # left = head--slow, root = slow.next right = slow.next.next--None
        slow, fast = head, head.next
        while fast:
            fast = None if not fast.next else fast.next.next
            slow = slow if not fast else slow.next
        root = TreeNode(slow.next.val)
        
        nexthead = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(nexthead)
        return root
        