# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###############################
############solution1##########

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        stack = []
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        curr_next = current.next
        while curr_next:
            for i in range(k):
                if curr_next:
                    stack.append(curr_next)
                    curr_next = curr_next.next
            #end_for
            if len(stack) != k:
                return dummy.next
            while len(stack):
                current.next = stack.pop()
                current = current.next
                print(current.val)
            #end
            current.next = curr_next
        #end_while
        
        return dummy.next


####################################
################solution2###########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        def reverse(pre: ListNode, k: int) -> ListNode:
            last = pre
            for i in range(k+1):
                last = last.next
                if i != k and last is None:
                    return None
            # 对pre  和  last 中间的节点做reverse
            tail = pre.next
            curr = pre.next.next
            while curr != last:
                curr_next = curr.next
                curr.next = pre.next
                pre.next = curr
                tail.next = curr_next
                curr = curr_next
            #end_while
            return tail
        ###
        while pre:
            pre = reverse(pre, k)
        return dummy.next