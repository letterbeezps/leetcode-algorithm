# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
写这题前先写206题
'''
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None
        if not(m-n):
            return head
        l = 0
        pre_node, next_node, node = None, None, head
        while node:
            l += 1
            pre_node = node if l == m-1 else pre_node
            next_node = node if l == n+1 else next_node
            node = node.next
            
        if m<1 or n>l or m>n:
            return None
        node = pre_node.next if pre_node else head
        node2 = node.next
        node.next = next_node
        
        while not(node2 is next_node):
            nn = node2.next
            node2.next = node
            node = node2
            node2 = nn
        
        if pre_node:
            pre_node.next = node
            return head
        else:
            return node
            
            