class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackValue = []
        self.stackMin = []
        

    def push(self, x: int) -> None:
        self.stackValue.append(x)
        if not self.stackMin or self.stackMin[-1] >= x:
            self.stackMin.append(x)
        

    def pop(self) -> None:
        if self.stackMin[-1] == self.stackValue[-1]:
            self.stackMin.pop()
        self.stackValue.pop()
        

    def top(self) -> int:
        return self.stackValue[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()