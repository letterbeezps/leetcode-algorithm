# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        dummyHead = ListNode(0)
        curr = dummyHead
        r_l1, r_l2 = self.reverseList(l1), self.reverseList(l2)
        p, q = r_l1, r_l2
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sumn = carry + x + y
            carry = sumn // 10
            curr.next = ListNode(sumn % 10)
            curr = curr.next
            p = p.next if p else None
            q = q.next if q else None
        if carry:
            curr.next = ListNode(carry)
            
        return self.reverseList(dummyHead.next)
            
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        curr = head
        pre = None
        
        while curr:
            curr.next, pre, curr = pre, curr, curr.next
        return pre
        