class NestedIterator(object):
    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.seq = collections.deque()  # 把嵌套列表直接变成结果数据
        self.cnt = 0
        self.dfs(nestedList)
        
    def dfs(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.seq.append(item.getInteger())
            else:
                self.dfs(item.getList())
        

    def next(self):
        """
        :rtype: int
        """
        t, self.cnt = self.cnt, self.cnt+1
        return self.seq[t]
    
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cnt < len(self.seq)