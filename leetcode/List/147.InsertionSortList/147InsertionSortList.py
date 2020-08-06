# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
review the insertion sort
https://github.com/letterbeezps/leetcode-algorithm/blob/master/DataStructure/Sort.md
'''
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode('0')
        dummy.next = head
        p = head.next
        head.next = None
        while p:
            #print(p.val)
            #print(dummy.next.val)
            current = ListNode(p.val)
            first, second = dummy, dummy.next
            # find the insert position
            while second and second.val < current.val:
                second = second.next
                first = first.next
            first.next = current
            current.next = second
            
            p = p.next
        return dummy.next
        