class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            curr_min = min(value, self.min_stack[-1])
            self.min_stack.append(curr_min)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()