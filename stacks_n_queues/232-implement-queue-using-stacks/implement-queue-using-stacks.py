class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        self.move_elements()
        return self.stack_out.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        # Ensure stack_out has the current elements in reversed order
        self.move_elements()
        return self.stack_out[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out


    def move_elements(self):
        """
        Helper method to move elements from stack_in to stack_out
        """
        # Only move elements if stack_out is empty to preserve FIFO order
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()