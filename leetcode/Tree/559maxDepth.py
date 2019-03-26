import collections
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root :
            return 0
        if not root.children:
            return 1
        length = 1+ max(self.maxDepth(node) for node in root.children)
        return length

    def maxDepth1(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_Depth = 0
        queue = collections.deque()  # 一个双端队列
        
        queue.append((root, max_Depth))
        while len(queue) > 0:
            current, depth = queue.popleft()
            
            if current and current.children:
                for child in current.children:
                    queue.append((child, depth + 1))
                    max_Depth = max(max_Depth, depth + 1)
            
        return max_Depth + 1

    def maxDepth2(self, root: 'Node') -> int:
        if root == None:
            return 0
        tmp = []
        for i in root.children:
            l = self.maxDepth(i)
            tmp.append(l)  
        return max(tmp) + 1 if tmp else 1