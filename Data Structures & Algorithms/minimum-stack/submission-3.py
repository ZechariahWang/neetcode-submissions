class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack: # if nothing inside the min stack, just add the value since its def gonna be the smallest value
            self.min_stack.append(value)
        elif value > self.min_stack[-1]: # if the current value is greater than the smallest value in the min stack, keep the current smallest value for next val
            self.min_stack.append(self.min_stack[-1])
        else: # if neither is satisfied, just add the value again (same command as the initial if statement)
            self.min_stack.append(value)
        
    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()