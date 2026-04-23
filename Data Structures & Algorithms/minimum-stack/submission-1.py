class MinStack:
    # Constructor to initialize the stack and min stack
    def __init__(self):
        # This stack stores all values
        self.stack = []

        # This stack keeps track of the minimum values
        self.minStack = []

    # This method adds a value to the stack
    def push(self, val: int) -> None:
        # Add the value to the main stack
        self.stack.append(val)

        # If minStack is empty, then push val as the first min
        if not self.minStack:
            self.minStack.append(val)
        else:
            # Compare val with the last min and push the smaller one
            current_min = self.minStack[-1]
            if val < current_min:
                self.minStack.append(val)
            else:
                self.minStack.append(current_min)

    # This method removes the top element from the stack
    def pop(self) -> None:
        # Remove the top element from both stacks
        self.stack.pop()
        self.minStack.pop()

    # This method returns the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # This method returns the current minimum element in the stack
    def getMin(self) -> int:
        return self.minStack[-1]
