# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        pre = ListNode(0)
        curPre = pre
        post = ListNode(0)
        curPost = post
        
        while head:
            if head.val < x:
                curPre.next = head
                curPre = curPre.next
                head = head.next
                curPre.next = None
            else:
                curPost.next = head
                curPost = curPost.next
                head = head.next
                curPost.next = None
        #end_while
        curPre.next = post.next
        return pre.next