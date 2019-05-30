# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
关键在于归并排序，并且是自底向上的归并排序
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p, n = head, 0
        while p:
            n += 1
            p = p.next
            
        dummy = ListNode(-1)
        dummy.next = head
        i = 1
        while i<n:
            begin = dummy
            j = 0
            while j+i < n:
                first = begin.next
                second = first
                for k in range(i): 
                    if second:
                        second=second.next
                #end_for
                f, s = 0, 0
                while f<i and s<i and second:
                    if first.val < second.val:
                        begin.next = first
                        begin = begin.next
                        first = first.next
                        f += 1
                    else:
                        begin.next = second
                        begin = begin.next
                        second = second.next
                        s += 1
                while f < i and first:
                    begin.next = first
                    begin = begin.next
                    first = first.next
                    f += 1
                while s < i and second:
                    begin.next = second
                    begin = begin.next
                    second = second.next
                    s += 1
                begin.next = second
                j += i*2
            #end_while
            i *= 2
        #end_while
        return dummy.next
        
            