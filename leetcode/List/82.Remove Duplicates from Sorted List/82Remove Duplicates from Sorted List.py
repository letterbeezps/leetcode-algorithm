# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        dummy = ListNode('#')
        dummy.next = head
        pre = dummy
        cur = head
        while cur.next:
            nxt = cur.next
            if cur.val == nxt.val:
                while nxt.next and nxt.val == nxt.next.val:
                    nxt = nxt.next
                pre.next = nxt.next
                cur = nxt.next
                if not cur:
                    return dummy.next
            else:
                pre = cur
                cur = nxt
                nxt = nxt.next
        return dummy.next          
        
            
        