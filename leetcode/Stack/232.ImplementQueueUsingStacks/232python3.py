# 使用python基本没什么难度
# 按照题意，我们需要使用两个栈来实现一个队列
# 栈是先进先出，第一个栈来执行入栈，再将第一个栈的元素POP出来
# 并按顺序入栈第二个栈，最后第二个栈的出栈顺序，就是第一个栈的入栈顺序
class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()