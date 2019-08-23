class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self, capacity=1000):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.getidx(key)
        node = self.data[idx]
        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.data[idx]
        self.data[idx] = new_node
                

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        node = self.data[self.getidx(key)]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.getidx(key)
        node = self.data[idx]
        pre = Node(-1,-1)
        head = pre
        pre.next = node
        
        while node:
            if node.key == key:
                pre.next = node.next
                break
            pre, node = node, node.next
        self.data[idx] = head.next
        
    def getidx(self, key) -> int:
        return key % self.capacity

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)