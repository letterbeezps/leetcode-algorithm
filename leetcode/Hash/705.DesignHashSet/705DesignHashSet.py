 class Node:
        
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self, capacity=1000):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity

    def add(self, key: int) -> None:
        # insert at the head of the list
        if not self.contains(key):
            idx = self.getidx(key)
            new_node = Node(key)
            new_node.next = self.data[idx]
            self.data[idx] = new_node
        

    def remove(self, key: int) -> None:
        idx = self.getidx(key)
        node = self.data[idx]
        pre = Node('dummy')
        head = pre
        pre.next = node
        while node:
            if node.val == key:
                pre.next = node.next
                break
            pre, node = node, node.next
            
        self.data[idx] = head.next
        
        # if node and node.val == key:
        #     self.data[idx] = node.next
        #     return
        # pre = None
        # while node:
        #     if node.val == key:
        #         pre.next = node.next
        #         return
        #     pre = node
        #     node = node.next
            
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self.getidx(key)
        node = self.data[idx]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False
    
    def getidx(self, key) -> int:
        return key % self.capacity
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)