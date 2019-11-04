# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import Counter

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        counter = Counter()
        for list in lists:
            while (list):
                counter[list.val] += 1
                list = list.next
        counter = sorted(counter.items(), key=lambda x:x[0])
        result = ListNode("dummy")
        orig = result
        for k in counter:
            a,b = k  # k now is a truple
            for i in range(b):
                new_node = ListNode(a)
                result.next = new_node
                result = new_node
        return orig.next


#####solution 2 PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        import queue
        self.index = 0
        que = queue.PriorityQueue()
        dummy = ListNode(0)
        if len(lists) == 0: return dummy.next
        current = dummy
        for l in lists:
            if l is not None:
                que.put((l.val, self.index, l))
                self.index += 1
                
        
        while not que.empty():
            node = que.get()[2]
            current.next = node
            current = current.next
            if node.next:
                que.put((node.next.val, self.index, node.next))
                self.index += 1
        return dummy.next