# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
其实就是求链表的倒数第k个元素
就是要处理一下k太大的情况
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        length, p = 0, head
        while p:
            length += 1
            p = p.next
        k %= length
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next