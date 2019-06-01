# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p = l1
        q = l2
        currentNode = dummyHead
        carry = 0  # 向前的进位
        while p or q:
            x = p.val if p else 0  # 取值，若当前节点唯空，取值为0
            y = q.val if q else 0
            sum = carry + x + y
            carry = sum // 10  # compute new carry
            currentNode.next = ListNode(sum % 10)  # get new node
            currentNode = currentNode.next
            p = p.next if p else None  
            q = q.next if q else None
            
        # end_while
        if carry > 0:
            currentNode.next = ListNode(carry)
        
        return dummyHead.next