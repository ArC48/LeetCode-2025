class MinStack:

    def __init__(self):
        self.storage = []

    def push(self, val: int) -> None:
        if not self.storage:
            self.storage.append((val, val))
        else:
            self.storage.append((val, min(val, self.storage[-1][1])))

    def pop(self) -> None:
        if self.storage:
            self.storage.pop()

    def top(self) -> int:
        if self.storage:
            return self.storage[-1][0]

    def getMin(self) -> int:
        if self.storage:
            return self.storage[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()