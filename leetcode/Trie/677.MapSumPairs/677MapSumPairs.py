class MapSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        we don't need flag "isword"
        """
        self.root = {}
        self.val = '#'
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            node = node.setdefault(c, {'#': 0})
        node[self.val] = val
        
    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            node = node.get(c)
            if not node:
                return 0
            
        return self.countValue(node)
        
    def countValue(self, node) -> int:
        res = node['#']
        for k, newNode in node.items():
            if k != '#':
                res += self.countValue(newNode)
                
        return res
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)