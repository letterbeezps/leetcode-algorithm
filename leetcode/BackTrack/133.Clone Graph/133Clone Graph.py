"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# 先复制每一个点，原点和新点之间的关系，维护哈希表
# 遍历所有边，在新点之间建立新的边
class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.Hash = {}
        
        if not node:
            return node
        p = Node(node.val, [])
        
        self.Hash[node] = p
        
        self.dfs(node)
        
        return p
    
    def dfs(self, node):
        for ver in node.neighbors:
            if ver not in self.Hash:
                self.Hash[ver] = Node(ver.val, [])
                self.dfs(ver)
            # 边
            self.Hash[node].neighbors.append(self.Hash[ver])