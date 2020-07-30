class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wrong_order_stack = []
        self.right_order_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.wrong_order_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.right_order_stack:
            return self.right_order_stack.pop()
        else:
            for i in range(len(self.wrong_order_stack)):
                self.right_order_stack.append(self.wrong_order_stack.pop())
            return self.right_order_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.right_order_stack:
            return self.right_order_stack[-1]
        else:
            for i in range(len(self.wrong_order_stack)):
                self.right_order_stack.append(self.wrong_order_stack.pop())
            return self.right_order_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.right_order_stack:
            if not self.wrong_order_stack:
                return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()