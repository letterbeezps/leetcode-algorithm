class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key is exit, put it at the tail
        # or just add it at the tail directly
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        
        if len(self.dic) > self.capacity:
            node_del = self.head.next
            del self.dic[node_del.key]
            self._remove(node_del)
        
    def _remove(self, node: Node):  
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    def _add(self, node: Node):
        # add at the tail
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


##########solution2
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self._ordered_dict = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        self._move_to_end_if_exits(key)
        
        return self._ordered_dict.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        self._move_to_end_if_exits(key)
        
        self._ordered_dict[key] = value
        if len(self._ordered_dict) > self._capacity:
            self._ordered_dict.popitem(last=False)  # FIFO
        
    def _move_to_end_if_exits(self, key: int) ->None:
        if key in self._ordered_dict:
            self._ordered_dict.move_to_end(key)