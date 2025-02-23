class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1) - 1):
            element = self.q1.pop(0)
            self.q2.append(element)
        elem = self.q1.pop(0)
        self.q1, self.q2 = self.q2, []
        return elem

    def top(self) -> int:
        last = 0
        for i in range(len(self.q1)):
            last = self.q1.pop(0)
            self.q2.append(last)
        self.q1, self.q2 = self.q2, []
        return last

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()