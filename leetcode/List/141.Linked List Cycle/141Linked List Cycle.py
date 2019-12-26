# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        first = second = head
        # 在环上，快慢指针一定会碰撞
        while first and second:
            first = first.next
            second = second.next
            if second:
                second = second.next
            
            if first == second:
                return True
        return False