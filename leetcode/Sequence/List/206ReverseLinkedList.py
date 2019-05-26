# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        curr = head
        pre = None
        while curr:
            curr_next = curr.next
            curr.next = pre
            pre = curr
            curr = curr_next
        return pre
        