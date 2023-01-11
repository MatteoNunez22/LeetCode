class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val < self.stack[-1][-1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][-1]))

    def pop(self) -> None:
        item = self.stack.pop(-1)
        return item[0]

    def top(self) -> int:
        item = self.stack[-1]
        return item[0]

    def getMin(self) -> int:
        item = self.stack[-1]
        return item[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()