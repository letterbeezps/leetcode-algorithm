# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
dummmy 1 2 3 4 5

'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        # swap current.next and current.next.next
        def swap2(pre: ListNode):
            dummy = pre.next
            pre.next = dummy.next
            dummy.next = dummy.next.next
            pre.next.next = dummy 
        
        while current.next and current.next.next:
            swap2(current)
            
            current = current.next.next
        return dummy.next
        